from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert.'),
    ('human', 'What is the capital of {country}?')
])

prompt = chat_template.invoke({
    'domain': 'AI',
    'country': 'India'
})

print(prompt)

# python 4.Prompts/chat_prompt_template.py