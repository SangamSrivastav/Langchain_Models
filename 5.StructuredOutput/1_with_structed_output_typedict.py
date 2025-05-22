from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import json

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

review_text = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
"""

prompt = f"""
Analyze the following customer review and return a JSON object with the following keys:
- summary: A 1-2 sentence summary of the review.
- sentiment: Either "positive", "negative", or "mixed".
- pros: A list of the positive points mentioned.
- cons: A list of the negative points mentioned.
- rating: An estimated rating out of 10.

Review:
\"\"\"{review_text}\"\"\"

Output the result only as a valid JSON object.
"""

response = model.invoke(prompt)

# Optional: clean up and parse JSON from response
try:
    result_json = json.loads(response.strip().split("```")[0])  # in case response has code block formatting
    print(json.dumps(result_json, indent=2))
except json.JSONDecodeError:
    print("Raw response:\n", response)
