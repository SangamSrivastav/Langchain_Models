import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load .env if needed
load_dotenv()

# Force override (hardcode or dynamically set)
os.environ["OPENAI_API_KEY"] = "sk-6c6648c7cd094fcd903aeb1eef05e8eb"

llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key=os.environ["OPENAI_API_KEY"],
    openai_api_base="https://api.deepseek.com"
)

response = llm.invoke("What is the capital of India?")
print("✅ Response:", response.content)
