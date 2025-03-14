from itertools import chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

openai_llm = ChatOpenAI(model="gpt-4o-mini")

messages = [
    ("system", "You are a facts expert who knows facts about {animal}."),
    ("human", "Tell me {fact_count} facts."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
print("-------This is Prompt Template---------")
print(prompt_template)

chain = prompt_template | openai_llm | StrOutputParser()
print("-------This is Chain---------")
print(chain)

result = chain.invoke({"animal": "pandas", "fact_count": 2})
print(result)