from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

model_name = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(model_name = model_name)

document = [
    "The capital of India is New Delhi.",
    "Paris is the capital of France.",
    "India's capital city is New Delhi.",
    "Apples are my favorite fruit.",
    "The Taj Mahal is located in Agra, India."
]

query = "What is the capital of India?"

doc_embeddings = embeddings.embed_documents(document)
query_embedding = embeddings.embed_query(query)

# Calculate cosine similarity
scores =cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x : x[1])[-1]

print(f"Query: {query}")
print(document[index])
print(f"Cosine Similarity Score: {score}")