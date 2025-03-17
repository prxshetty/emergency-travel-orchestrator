import json
import re
from typing import Dict, Any


def pretty_print_response(turn_number: int, response: Dict[str, Any]) -> None:
    print(f"\n{'='*80}")
    print(f"TURN {turn_number} RESPONSE")
    print(f"{'='*80}")
    
    if "messages" in response:
        for msg in response["messages"]:
            try:
                role = getattr(msg, "type", "unknown")
                content = getattr(msg, "content", "")
            except (AttributeError, TypeError):
                role = msg.get("role", "unknown") if isinstance(msg, dict) else "unknown"
                content = msg.get("content", "") if isinstance(msg, dict) else str(msg)            
            if role.lower() == "human" or role.lower() == "user":
                print(f"\n👤 USER:\n{'-'*40}")
                print(f"{content}")
            elif role.lower() == "ai" or role.lower() == "assistant":
                agent_match = re.search(r"\[(.*?)\]", content[:50])
                agent_name = agent_match.group(1) if agent_match else "AI Assistant"
                if agent_match:
                    content = content.replace(agent_match.group(0), "").strip()
                
                print(f"\n🤖 {agent_name.upper()}:\n{'-'*40}")
                print(f"{content}")
            else:
                print(f"\n📝 {role.upper()}:\n{'-'*40}")
                print(f"{content}")
    else:
        print(json.dumps(response, indent=2))
    
    print(f"\n{'='*80}\n")


def print_scenario_menu(scenarios: Dict[str, Dict[str, str]]) -> None:
    print("\n" + "="*50)
    print("EMERGENCY TRAVEL RESPONSE SYSTEM - SCENARIO SELECTION")
    print("="*50)
    
    for key, scenario in scenarios.items():
        print(f"\n[{key}] {scenario['name']}")
        print(f"    {scenario['description']}")


def print_scenario_header(choice: str, scenario: Dict[str, str]) -> None:
    print(f"\n{'*'*100}")
    print(f"SCENARIO {choice}: {scenario['name']}")
    print(f"{'*'*100}")
    print(f"\nINITIAL SITUATION: {scenario['initial']}")
    print(f"{'*'*100}\n")


def print_followup_header(followup_text: str) -> None:
    print(f"\n{'*'*50}")
    print(f"FOLLOW-UP: {followup_text}")
    print(f"{'*'*50}\n") 