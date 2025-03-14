from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM
openai_llm = ChatOpenAI(model="gpt-4o-mini")

# Define the template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Give me a short summary about {topic}."
)
print("------This is prompt-template---------")
print(prompt_template)

prompt = prompt_template.format(topic="Machine Learning")
print("------This is prompt---------")
print(prompt)


# Generate response using formatted prompt
response = openai_llm.invoke(prompt)
print(response)
