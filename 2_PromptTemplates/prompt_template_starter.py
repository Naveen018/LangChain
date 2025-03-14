from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

openai_llm = ChatOpenAI(model="gpt-4o-mini")

template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max"

prompt_template = ChatPromptTemplate.from_template(template)
print("-------This is Prompt Template---------")
print(prompt_template)

prompt =  prompt_template.invoke({
    "tone": "professional", 
    "company": "samsung", 
    "position": "AI Engineer", 
    "skill": "AI"
})
print("-------This is Prompt---------")
print(prompt)

result = openai_llm.invoke(prompt)
print(result.content)