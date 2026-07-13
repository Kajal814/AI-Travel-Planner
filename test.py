from llm import llm

response = llm.invoke("Say Hello in one sentence.")

print(response.content)