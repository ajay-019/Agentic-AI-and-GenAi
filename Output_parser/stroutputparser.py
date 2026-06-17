from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token="xyz"
)
model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']   # was 'input_variable' (typo) - correct kwarg is plural
)

template2 = PromptTemplate(
    template='write 5 line summary on {text}',
    input_variables=['text']    # same fix here
)

parser = StrOutputParser()

# Chain 1: prompt -> model -> parser
# parser.invoke gives you a plain string directly, no need for result.content
chain1 = template1 | model | parser
result = chain1.invoke({'topic': 'black hole'})

# Chain 2: feed chain1's output into the summary prompt
chain2 = template2 | model | parser
result1 = chain2.invoke({'text': result})

print(result1)