# CrewAI Project Documentation

## Brief Introduction to CrewAI

CrewAI is an innovative project aimed at leveraging the power of large language models (LLMs) for enhancing automation and intelligence in various applications. By integrating state-of-the-art models, CrewAI seeks to provide robust solutions for natural language processing, understanding, and generation, aiming to revolutionize how businesses and developers interact with AI technologies.

Crew-ai system architecture:
![Crew-AI Component](/media/crewai-diagram2.jpg "Crew-AI Component")


## Setting Up Your Project

### Installing Required Libraries

To set up your project environment, begin by installing the necessary libraries. Run the following command in your terminal:

```bash
pip install -r requirements.txt
```

### Configuration

For the project to function correctly, you need to configure the environment variables. Create a `.env` file in your project directory and include the following information:

```plaintext
LANGCHAIN_API_KEY="Your_Langchain_API_Key_Here"
LANGCHAIN_PROJECT="CREW_AI"
LANGCHAIN_TRACING_V2="true"
EXA_API_KEY="Your_Exa_API_Key_Here"
OPENAI_API_BASE='http://localhost:11434/v1'
OPENAI_MODEL_NAME='crewai-llama2'
OPENAI_API_KEY=Your_OpenAI_API_Key_Here
```

**Important:** Ensure not to share your API keys publicly.

### Setting Up Ollama

Ollama is a tool used for managing and deploying large language models. To install Ollama and set up the necessary models, follow these steps:

1. Install Ollama:

Download & Install ollama from its website 

https://ollama.com/

2. Pull the Llama2 model:

```bash
ollama pull llama2
```

3. Create a customized version of the Llama2 model for the CrewAI project:

```bash
ollama create crewai-llama2 -f ./Llama2Modelfile
```

This command will create a Large Language Model specifically tailored for CrewAI.

Crew-AI architectue calls:
![Crew-AI Component](/media/crewai-diagram1.jpg "Crew-AI Component")
### Additional Resources

For more information or to obtain API keys, visit the following resources:

- **Exa API:** [https://exa.ai/](https://exa.ai/)
- **Langchain:** [https://langchain.com/](https://langchain.com/)

Following these steps will set up your project with CrewAI, integrating cutting-edge language models to power your applications.

Interection between crew-ai Agents, Task and Tools
![Crew-AI Component](/media/crewai-diagram.jpg "Crew-AI Component")