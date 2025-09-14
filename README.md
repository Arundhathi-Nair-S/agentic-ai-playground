# 🤖 Agentic AI Playground

A hands-on exploration of AI agents using Google's Agent Development Kit (ADK). This repository contains practical examples and experiments with different types of AI agents, from basic conversational agents to tool-enabled agents that can interact with external services.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Conda (recommended for environment management)
- Google ADK access and API keys

### Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd agentic-ai-playground
   ```

2. **Create and activate the conda environment:**
   ```bash
   conda create -n agentic-ai-playground python=3.10
   conda activate agentic-ai-playground
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory with your API keys:
   ```bash
   # Add your Google API keys and other required credentials
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Run the web interface:**
   ```bash
   adk web
   ```

## 📁 Project Structure

```
agentic-ai-playground/
├── 1-basic-agent/          # Simple conversational agent
│   └── greeting_agent/     # Basic greeting and conversation capabilities
├── 2-tool-agent/           # Agent with external tool integration
│   └── tool_agent/         # Google Search + custom time tool
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🧪 Experiments

### 1. Basic Agent (`1-basic-agent/`)

A foundational conversational agent that demonstrates:
- Basic dialogue capabilities
- Agent initialization and configuration
- Simple response generation

**Features:**
- Conversational AI using Gemini 2.0 Flash
- Basic greeting and interaction patterns

### 2. Tool Agent (`2-tool-agent/`)

An enhanced agent that showcases tool integration:
- External API integration (Google Search)
- Custom Python function tools
- Time-based utilities

**Features:**
- **Google Search Integration:** Real-time web search capabilities
- **Custom Time Tool:** Get current time in formatted output
- **Model:** Gemini 2.0 Flash for enhanced reasoning

**Important Notes:**
- Currently, ADK supports only one tool per agent
- Custom tools cannot be combined with built-in tools in the same agent
- Custom tools require proper docstrings and return type annotations

## 🛠️ Technology Stack

- **Google ADK**: Agent Development Kit for building AI agents
- **Gemini 2.0 Flash**: Google's latest language model
- **Python Tools**: Custom function integration
- **External APIs**: Google Search, Yahoo Finance
- **Development Tools**: Black, isort, pre-commit for code quality

## 📚 Key Concepts Learned

### Agent Design Patterns
- **Single Tool Limitation**: Each agent can only use one tool at a time
- **Tool Documentation**: Custom tools require comprehensive docstrings
- **Return Types**: All custom tools must specify return types for proper integration

### Custom Tool Development
```python
def get_current_time() -> dict:
    """
    Get the current time in the format of YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
```

### Agent Configuration
```python
root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="You are a helpful assistant...",
    tools=[google_search]  # Single tool limitation
)
```

## 🚀 Running Individual Agents

### From Root Directory
```bash
adk web  # Discovers and loads all agents
```

### From Specific Agent Directory
```bash
cd 2-tool-agent
adk web  # Runs only the tool agent
```

## 🔧 Development

### Code Quality
This project uses several tools to maintain code quality:
- **Black**: Code formatting
- **isort**: Import sorting
- **pre-commit**: Git hooks for automated checks

### Adding New Agents

1. Create a new directory: `3-your-agent/`
2. Create the agent structure:
   ```
   3-your-agent/
   ├── __init__.py          # Export agent as 'agent'
   └── your_agent/
       ├── __init__.py
       └── agent.py         # Define your agent
   ```
3. Export your agent properly in `__init__.py`:
   ```python
   from .your_agent.agent import root_agent as agent
   ```

## 🐛 Troubleshooting

### Common Issues

1. **Module Import Errors**: Ensure proper `__init__.py` files and correct agent exports
2. **Tool Integration**: Remember the one-tool-per-agent limitation
3. **Environment Variables**: Check that all required API keys are set

### Import Structure
The ADK web command expects each module to export an `agent` attribute:
```python
# In your module's __init__.py
from .your_agent.agent import root_agent as agent
```

## 📈 Future Enhancements

- [ ] Multi-tool agent exploration (when ADK supports it)
- [ ] Database integration agents
- [ ] File system manipulation agents
- [ ] API orchestration agents
- [ ] Agent-to-agent communication patterns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run code quality checks
5. Submit a pull request

## 📄 License

[Add your license information here]

## 🔗 Resources

- [Google ADK Documentation](https://developers.google.com/adk)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Agent Design Best Practices](https://developers.google.com/adk/concepts)

---

**Happy Agent Building! 🤖✨**
