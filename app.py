""" 
# App to replicate ChatGPT using Chainlit

Usage : chainlit run app.py -w
"""
import os
from dotenv import find_dotenv, load_dotenv
from langchain.llms import AzureOpenAI
import os
from langchain import PromptTemplate, LLMChain
import chainlit as cl

_ = load_dotenv(find_dotenv())

os.environ["OPENAI_API_TYPE"] = os.getenv("api_type")
os.environ["OPENAI_API_BASE"] = os.getenv("api_base")
os.environ["OPENAI_API_VERSION"] = os.getenv("api_version")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = AzureOpenAI(
    deployment_name="chatgpt-gpt35-turbo",
    model_name="gpt-35-turbo",
    temperature = 0,
    max_tokens = 800,
)

template = """Question: {question}

Answer: Let's think step by step."""


@cl.langchain_factory
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    return llm_chain