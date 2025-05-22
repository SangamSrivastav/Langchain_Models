from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  # ✅ A proper, free, chat-friendly model
    task="text-generation",
)

chat_history = [
    SystemMessage(
        content="You are a helpful assistant. You can answer questions and provide information on various topics."
    )
]

while True:
    user_input = input("Enter your prompt (or 'exit' to quit): ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    response = model.invoke(user_input)
    chat_history.append(AIMessage(content=response))
    print("AI: ",response)

print("Chat History:")

# python 4.Prompts/chatbot.py