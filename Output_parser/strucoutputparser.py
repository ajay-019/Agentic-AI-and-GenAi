from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token="xyz"
)
model = ChatHuggingFace(llm=llm)

Schema=[
    ResponseSchema(name="fact_1", description="First fact about the topic"),
    ResponseSchema(name="fact_2", description="Second fact about the topic"),
    ResponseSchema(name="fact_3", description="Third fact about the topic")]
output_parser = StructuredOutputParser.from_response_schemas(Schema)

template = PromptTemplate(
    template="Provide three facts about the topic: {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions': output_parser.get_format_instructions()}
)


chain = template | model | output_parser

result = chain.invoke({'topic': 'Ajay Meena IITb linkedin profile'})
print(result)

# prompt = template.invoke(topic="Ajay Meena IITb")
# result = model(prompt)
# parsed_result = output_parser.parse(result.content)
# print(parsed_result)