""" 
chainlit run text2sql.py -w
"""
import chainlit as cl
import openai
import os
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

os.environ["OPENAI_API_TYPE"] = os.getenv("api_type")
os.environ["OPENAI_API_BASE"] = os.getenv("api_base")
os.environ["OPENAI_API_VERSION"] = os.getenv("api_version")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

prompt = """SQL tables (and columns):
* Customers(customer_id, signup_date)
* Streaming(customer_id, video_id, watch_date, watch_minutes)

A well-written SQL query that {input}:
```"""

model_name = "text-davinci-003"

settings = {
    "temperature": 0,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": ["```"]
}

@cl.on_message
def main(message: str):
    fromatted_prompt = prompt.format(input=message)
    response = openai.Completion.create(
        engine=model_name,
        prompt=fromatted_prompt,
        **settings
    )
    content = response["choices"][0]["text"]

    cl.Message(
        content=content,
        language="sql",
        prompt=fromatted_prompt,
        llm_settings=cl.LLMSettings(model_name=model_name, **settings)
    ).send()