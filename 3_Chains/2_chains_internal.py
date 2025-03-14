from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence

load_dotenv()

openai_llm = ChatOpenAI(model="gpt-4o-mini")

messages = [
    ("system", "You are a facts expert who knows facts about {animal}."),
    ("human", "Tell me {fact_count} facts."),
]

def format_templates(messages):
    return ChatPromptTemplate.from_messages(messages)

def replace_placeholders(inputs):
    prompt_template = format_templates(messages)
    return prompt_template.format(**inputs)

def invoke_llm(formatted_prompt):
    return openai_llm.invoke(formatted_prompt)

def parse_result(result):
    return result.content

# Create Runnables
format_runnable = RunnableLambda(format_templates)
replace_runnable = RunnableLambda(replace_placeholders)
invoke_runnable = RunnableLambda(invoke_llm)
result_runnable = RunnableLambda(parse_result)

# Chain them using RunnableSequence
pipeline = RunnableSequence(format_runnable, replace_runnable, invoke_runnable, result_runnable)

# Run the pipeline
result = pipeline.invoke({"animal": "cat", "fact_count": 1})
print(result)
