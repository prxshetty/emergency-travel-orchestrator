import time
import os
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph_swarm import create_swarm
from langgraph.store.memory import InMemoryStore
from dotenv import load_dotenv
from agents.agent_definitions import create_agents
from utils.formatting import pretty_print_response, print_scenario_menu, print_scenario_header, print_followup_header
from utils.invocation import invoke_with_retry
from scenarios.emergency_scenarios import get_scenarios
load_dotenv()

def main():
    model = ChatOpenAI(model="gpt-4", temperature=0.2)    
    agents = create_agents(model)    
    checkpointer = InMemorySaver()
    store = InMemoryStore()    
    workflow = create_swarm(
        list(agents.values()),
        default_active_agent="EmergencyCoordinator"
    )    
    app = workflow.compile(checkpointer=checkpointer, store=store)    
    scenarios = get_scenarios()
    print_scenario_menu(scenarios)
    while True:
        choice = input("\nSelect a scenario number (1-6): ")
        if choice in scenarios:
            break
        print("Invalid choice. Please select a number between 1 and 6.")
    
    selected = scenarios[choice]    
    config = {"configurable": {"thread_id": f"emergency-{choice}"}}    
    print_scenario_header(choice, selected)
    
    try:
        turn_1 = invoke_with_retry(
            app,
            {"messages": [{"role": "user", "content": selected['initial']}]},
            config
        )
        pretty_print_response(1, turn_1)        
        print_followup_header(selected['followup'])        
        turn_2 = invoke_with_retry(
            app,
            {"messages": [{"role": "user", "content": selected['followup']}]},
            config
        )
        pretty_print_response(2, turn_2)
        additional_input = input("\nWould you like to ask a follow-up question? (y/n): ")
        if additional_input.lower() == 'y':
            user_followup = input("\nEnter your follow-up question: ")
            print_followup_header(f"USER: {user_followup}")            
            turn_3 = invoke_with_retry(
                app,
                {"messages": [{"role": "user", "content": user_followup}]},
                config
            )
            pretty_print_response(3, turn_3)
        
    except Exception as e:
        print(f"Error processing scenario: {str(e)}")
        print("Try checking your API key, model availability, and network connection.")


if __name__ == "__main__":
    main()