# Emergency Travel Response System

A sophisticated multi-agent system leveraging LangGraph's Swarm architecture, langSmith and OpenAI to coordinate emergency travel assistance. This system demonstrates advanced agent collaboration for handling complex travel emergencies through specialized AI agents.

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![LangChain](https://img.shields.io/badge/langchain-latest-orange.svg)](https://python.langchain.com/)
[![LangSmith](https://img.shields.io/badge/langsmith-latest-blue.svg)](https://smith.langchain.com/)

##  Features

- **Multi-Agent Collaboration**: Specialized agents working together to handle complex emergencies
- **Real-time Monitoring**: Integration with LangSmith for comprehensive tracing and debugging
- **Scenario-based Testing**: Pre-built emergency scenarios to test system capabilities
- **Fault Tolerance**: Built-in retry mechanisms and error handling
- **Modular Architecture**: Easy to extend with new agents, tools, and scenarios
- **Interactive Follow-ups**: Ability to ask additional questions and get real-time responses

##  Agent Ecosystem

Our system includes specialized agents for different aspects of travel emergencies:

| Agent | Role | Primary Responsibilities |
|-------|------|------------------------|
| Emergency Coordinator | Central Orchestrator | Triage requests, delegate tasks, coordinate responses |
| Medical Evacuation Specialist | Medical Emergency Handler | Assess medical situations, arrange evacuations |
| Disaster Response Expert | Natural Disaster Specialist | Handle evacuations, assess disaster impacts |
| Security Analyst | Security Expert | Evaluate threats, provide safety guidance |
| Documentation Expert | Travel Document Specialist | Handle visa/passport emergencies |
| Accommodation Finder | Housing Specialist | Secure emergency accommodation |
| Communication Coordinator | Communication Expert | Establish reliable communication channels |
| Medical Advisor | Health Consultant | Provide medical guidance and recommendations |
| Local Resource Locator | Local Support Specialist | Connect with local emergency services |

##  Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/emergency-travel-response.git
   cd emergency-travel-response
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   # On Unix/macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the root directory:
   ```env
   # Required
   OPENAI_API_KEY=your_openai_api_key

   # Optional (for LangSmith monitoring)
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_API_KEY=your_langsmith_api_key
   LANGCHAIN_PROJECT=emergency-travel-response
   ```

## Usage

1. **Start the system**
   ```bash
   python main.py
   ```

2. **Select a scenario** from the available emergency situations:
   - Medical emergencies
   - Security threats
   - Natural disasters
   - Documentation emergencies
   - Communication crises
   - Complex multi-aspect scenarios

3. **Follow the interactive prompts** to see how the agents handle the situation

## Monitoring with LangSmith

### Setup
1. Create an account at [LangSmith](https://smith.langchain.com/)
2. Get your API key from the dashboard
3. Add LangSmith environment variables to your `.env` file
4. Run the system to start collecting data

### Monitoring Features
- **Trace Visualization**: See the flow of agent interactions
- **Performance Metrics**: Monitor response times and token usage
- **Debug Tools**: Analyze agent decision-making processes
- **Scenario Analytics**: Track performance across different emergency types

## Project Structure

- `agents/`: Contains the definitions of all specialized agents
- `tools/`: Contains the emergency tools implementation
- `utils/`: Contains utility functions and formatting
- `scenarios/`: Contains emergency scenario definitions
- `main.py`: The main application entry point
- `requirements.txt`: Project dependencies

##  Extending the System

### Adding New Tools
Add new emergency tools in `tools/emergency_tools.py`:
```python
def new_emergency_tool(param1: str, param2: int) -> Dict[str, Any]:
    """
    Tool description and documentation
    """
    # Tool implementation
    return {"result": "tool_output"}
```

### Creating New Agents
Define new agents in `agents/agent_definitions.py`:
```python
new_specialist = create_react_agent(
    model,
    [tool1, tool2],
    prompt="""Agent prompt and instructions""",
    name="NewSpecialist"
)
```

### Adding New Scenarios
Add scenarios in `scenarios/emergency_scenarios.py`:
```python
"new_scenario": {
    "name": "Scenario Name",
    "description": "Scenario description",
    "initial": "Initial situation...",
    "followup": "Follow-up development..."
}
```

## Contribution

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- LangChain team for the excellent framework, specifically this YouTube video on building agent swarms: https://www.youtube.com/watch?v=4oC1ZKa9-Hs

## Screenshots

[Coming Soon] Screenshots demonstrating the system in action will be added here.

## Future Enhancements
- [ ] Integration with real-world emergency services APIs ( TavilyAPI, SerpAPI for actual accomodations, travel expense)
- [ ] Mobile application interface ( Locally Hosted LLMs on Devices (<4B) should be able to fulfill this task perfectly)
- [ ] Multi-language support ( If this scales )
- [ ] Enhanced security protocols ( Currently has none)
- [ ] Automated testing suite
- [ ] Performance optimization for large-scale deployments
- [ ] Support for multiple LLM providers (OpenRouter, Anthropic, Tavily, etc.) with easy provider switching

