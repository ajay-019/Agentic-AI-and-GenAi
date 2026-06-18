from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token="xyz"
)
model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str = Field(description='Name of the famous person in rajasthan ')
    age:int = Field(gt=18,description='age of the person')
    city:str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Provide the name, age and city of a famous person in rajasthan \n {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# prompt=template.invoke({})
# result=model.invoke(prompt)
# parsed_result=parser.parse(result.content)
# print(parsed_result)
chain = template | model | parser
result = chain.invoke({})
print(result)