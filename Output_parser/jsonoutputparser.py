from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token="xyz"
)
model = ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template =PromptTemplate(
    template='Giv me 5 facts about input topic {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'topic': 'Neem Ka Thana'})
print(result)

# prompt = template.format()

# print(prompt)

# result = model.invoke(prompt)

# print(parser.parse(result.content))