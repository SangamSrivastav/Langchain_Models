from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  # ✅ A proper, free, chat-friendly model
    task="text-generation",
)

response = llm.invoke("What is the capital of India?")
print(response)
