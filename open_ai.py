from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model = "gpt-5",
    input = "Write a short story about a unicorn."
)

print(response)