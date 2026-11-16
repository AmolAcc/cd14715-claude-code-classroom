import anthropic

client = anthropic.Anthropic(
    base_url="https://claude.vocareum.com",
    # api_key is read from ANTHROPIC_API_KEY env var automatically
)

response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)