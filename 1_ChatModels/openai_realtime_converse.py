from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

openai_llm = ChatOpenAI(model="gpt-4o-mini")

chat_history = []

system_message = SystemMessage(content="You are an useful AI assistant.")
chat_history.append(system_message)

# chat loop
while True:
    query = input("You: ")
    if query.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=query))
    
    result = openai_llm.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    
    print(f"AI: {response}")
    
print("------Message History-------")
print(chat_history)