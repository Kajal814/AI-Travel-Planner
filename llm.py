from dotenv import load_dotenv
import os

from langchain_cohere import ChatCohere


load_dotenv()


llm = ChatCohere(
    model="command-a-03-2025",
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    temperature=0.7
)