from langchain.embeddings import HuggingFaceEmbeddings

model_name = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(
    model_name=model_name
)
# Example text
text = "This is an example sentence to be embedded."
# Get the embedding 
query_result = embeddings.embed_query(text)
print(query_result)