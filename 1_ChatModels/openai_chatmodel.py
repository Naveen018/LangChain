from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

openai_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=500)

result = openai_llm.invoke("Tell me a Joke: ")

print(result.content)