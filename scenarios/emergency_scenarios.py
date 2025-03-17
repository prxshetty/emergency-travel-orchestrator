from typing import Dict, Any

def get_scenarios() -> Dict[str, Dict[str, str]]:
    """
    Return a dictionary of available emergency scenarios.
    
    Each scenario includes:
    - name: Short descriptive name
    - description: Longer explanation of the scenario
    - initial: The initial user query that starts the scenario
    - followup: A follow-up message to continue the conversation
    
    Returns:
        Dictionary of scenario definitions
    """
    return {
        "1": {
            "name": "Medical Emergency",
            "description": "A colleague experiencing chest pain in Japan",
            "initial": "I need urgent help. My colleague is experiencing chest pain while traveling in Japan for business. What should we do?",
            "followup": "The pain is on the left side of his chest, and he's also feeling dizzy. He has a history of high blood pressure."
        },
        "2": {
            "name": "Security Threat",
            "description": "A traveler in a region with increasing civil unrest",
            "initial": "I'm currently in Cairo, Egypt and there are reports of protests growing in the city center. I'm concerned about my safety at my hotel which is near Tahrir Square.",
            "followup": "The protests are getting closer to my hotel. I can hear loud noises and see police. I'm traveling alone and don't speak Arabic."
        },
        "3": {
            "name": "Documentation Emergency",
            "description": "Lost passport and urgent border crossing needed",
            "initial": "I've lost my passport while traveling in Italy and need to get to Germany for an urgent family emergency within 24 hours. What can I do?",
            "followup": "I'm a US citizen and I have a photocopy of my passport and my driver's license with me. The family emergency is my father being hospitalized."
        },
        "4": {
            "name": "Natural Disaster & Accommodation",
            "description": "Travelers needing evacuation and shelter after earthquake",
            "initial": "We're a family of 4 in Mexico City and there was just a major earthquake. Our hotel has been evacuated and declared unsafe. We need somewhere to stay and information about getting back to the United States.",
            "followup": "We have two children ages 5 and 7, and my mother-in-law uses a wheelchair. We still have our passports but very limited cash. We're not sure if our return flights in 3 days will still operate."
        },
        "5": {
            "name": "Communication Crisis",
            "description": "Establishing contact during infrastructure disruption",
            "initial": "I'm trying to reach my team of 5 engineers who were in Thailand during the major flooding. Cell networks seem to be down and I haven't heard from them in 24 hours.",
            "followup": "Their last known location was Bangkok, in the eastern part of the city. They were staying at different hotels and working on a project at a local manufacturing facility."
        },
        "6": {
            "name": "Complex Multi-Tool Scenario",
            "description": "Scenario designed to trigger most or all specialized agents",
            "initial": "Our corporate executive team of 6 people is stranded in Ukraine due to sudden border closures and flight cancellations. One executive has a heart condition, we've lost contact with two team members, our hotel has received a security threat, and most of the team's travel documents were left in a vehicle that's now inaccessible. We need comprehensive emergency assistance.",
            "followup": "The executive with the heart condition is now reporting chest pain and shortness of breath. We need medical help, secure transportation to the Polish border, emergency documentation assistance, and a way to establish reliable communication with our two missing team members."
        }
    } 