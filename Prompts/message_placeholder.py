from langchain_core.prompts import ChatPromptTemplate,MessagePlaceholder

chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful customer support assistant'),
    MessagePlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])
