import random
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')

random_topics = ["health", "career", "finance", "love", "family", "investments", "friendships", "opportunities"]

# Access a random value from the list using the built-in random module
random_value = random.choice(random_topics)

open_ai_completion_and_topic = {"completion": "", "topic": random_value}

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": 'system', "content": 'You are a helpful assistant.'},
        {
            "role": 'user',
            "content": f"Give a one-sentence new year about {random_value} in a first person narrative",
        },
        {"role": 'assistant', "content": "Be very practical and direct about expectations. Don't list categories. Your response should be conversational."},
    ],
    stream=True,
)

# Capture responses in a list
responses = []

for chunk in stream:
    try:
        if chunk.choices[0].delta.content is not None:
            open_ai_completion_and_topic["completion"] += chunk.choices[0].delta.content
            open_ai_completion_and_topic["completion"] = open_ai_completion_and_topic["completion"].replace("'", "")
    except Exception as e:
        print(f"Error occurred while processing chunk: {str(e)}")

# Add the completed response to the list
responses.append(open_ai_completion_and_topic.copy())

# Make sure the completion is not an empty string. if so, the chunk never assigned the content meaning an exception was thrown
def ai_resolution():
    try:
        resolution = responses[0]
        if len(resolution["completion"]) > 0:
            return resolution
    except Exception as e:
        return {"error": f"There is a problem with our AI ({str(e)}). Contact support"}


# Use the ai_resolution function in other files
result = ai_resolution()