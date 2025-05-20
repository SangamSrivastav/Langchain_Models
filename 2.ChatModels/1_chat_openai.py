from langchain.chat_models import GPT4All

llm = GPT4All(model="ggml-gpt4all-j-v1.3-groovy")

response = llm.invoke("What is the capital of India?")
print(response.content)
