from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#Chat template with MessagesPlaceholder
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer service agent.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{quert}')
])

chat_history = []
#Load chat history

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'What is the status of my order?'})
print(prompt)