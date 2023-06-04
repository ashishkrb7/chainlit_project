# ChainLit Framework for Chatbot using ChatGPT

## Introduction
 
ChainLit is a framework that can be used to create a chatbot using the ChatGPT model. It provides a simple and easy-to-use interface for developers to build conversational agents. ChatGPT is an AI model that can generate human-like responses to text inputs. It is pre-trained on a large dataset and can be fine-tuned to specific use cases.

## Installation

- Install [Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Windows-x86_64.exe) from https:/.conda.io/en/latest/miniconda.html#windows-installers (for python)

- After Anaconda installation, go to search and run Anaconda Prompt and create virtual environment using following commands

    `conda create -y -n gpt python=3.11.0`

- Activate the conda environment

    `conda activate gpt`
    
- Clone the repository to your local machine. 

    `git clone https://github.com/ashishkrb7/chainlit_project.git` 

- Go to working directory

    `cd chainlit_project`

- Install the required dependencies using 

    `python -m pip install -r requirements.txt`

- Create .env file. It should contain following information

    ```txt
    api_type = 
    api_base = 
    api_version = 
    OPENAI_API_KEY = 
    ```

## Description

ChainLit provides a simple API for developers to build a chatbot using ChatGPT. It handles the input and output of text data to the model and allows developers to focus on building the conversational flow.

>app.py

The app can be run using the command `chainlit run app.py -w`. The script imports necessary modules such as os, dotenv, and langchain. It loads environment variables using dotenv and creates an instance of AzureOpenAI for language modeling. The script also defines a template for the input prompt, and a factory function that creates a PromptTemplate object and an LLMChain object using the loaded language model. The LLMChain object is returned by the factory function and can be used to generate responses to user input.

## Conclusion
 
ChainLit provides a simple and easy-to-use framework for building chatbots using ChatGPT. It handles the input and output of text data to the model and allows developers to focus on building the conversational flow. With ChainLit, developers can quickly build and deploy chatbots for a variety of use cases.

## References 

https://docs.chainlit.io/overview
