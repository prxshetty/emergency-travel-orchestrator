import json
from typing import Dict, List, Any
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_handoff_tool, create_swarm
from langgraph.store.memory import InMemoryStore
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4o")

def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

def create_agents():
    """Create and configure the agent ensemble."""
    # Initialize the language model
    model = ChatOpenAI(model="gpt-4o")

    # Create Alice: the addition expert
    alice = create_react_agent(
        model,
        [add, create_handoff_tool(agent_name="Bob")],
        prompt="You are Alice, an addition expert.",
        name="Alice",
    )

    # Create Bob: the pirate speaker
    bob = create_react_agent(
        model,
        [create_handoff_tool(agent_name="Alice", description="Transfer to Alice, she can help with math")],
        prompt="You are Bob, you speak like a pirate.",
        name="Bob",
    )
    
    return alice, bob

def pretty_print_response(turn_number: int, response: Dict[str, Any]):
    """Format and print the agent response in a readable way."""
    print(f"\n{'='*50}")
    print(f"TURN {turn_number} RESPONSE")
    print(f"{'='*50}")    
    if "messages" in response:
        for msg in response["messages"]:
            role = getattr(msg, "type", "unknown")
            content = getattr(msg, "content", "")
            print(f"{role.upper()}: {content}")
    else:
        print(json.dumps(response, indent=2))
    print(f"{'='*50}\n")

def main():
    alice, bob = create_agents()
    checkpointer = InMemorySaver()
    store = InMemoryStore()
    workflow = create_swarm(
        [alice, bob],
        default_active_agent="Alice"
    )
    app = workflow.compile(checkpointer=checkpointer, store = store)    
    config = {"configurable": {"thread_id": "1"}}
    
    # First interaction: Ask to speak to Bob
    turn_1 = app.invoke(
        {"messages": [{"role": "user", "content": "I'd like to speak to Bob"}]},
        config,
    )
    pretty_print_response(1, turn_1)
    
    # Second interaction: Ask a math question
    turn_2 = app.invoke(
        {"messages": [{"role": "user", "content": "What's 5 + 7?"}]},
        config,
    )
    pretty_print_response(2, turn_2)

if __name__ == "__main__":
    main()