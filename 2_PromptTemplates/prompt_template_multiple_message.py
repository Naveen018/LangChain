from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

openai_llm = ChatOpenAI(model="gpt-4o-mini")

messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
print("-------This is Prompt Template---------")
print(prompt_template)

prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
print("-------This is Prompt---------")
print(prompt)

result = openai_llm.invoke(prompt)
print(result.content)