from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

openai_llm = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(content="You are an expert in social media content strategy."),
    HumanMessage(content="Give me a short tip to create engaging posts on Instagram."),
    AIMessage(content="To create engaging posts on Instagram, focus on storytelling. Share a personal anecdote or a behind-the-scenes look that resonates with your audience. Use high-quality visuals, and pair them with a compelling caption that invites interactions—ask questions or encourage followers to share their own experiences in the comments. This not only creates a personal connection but also boosts engagement!"),
    HumanMessage(content="I have visited kumbhmela recently. What captions can I write about it?"),
]

result = openai_llm.invoke(messages)

print(result.content)