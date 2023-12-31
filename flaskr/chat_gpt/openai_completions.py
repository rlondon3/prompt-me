import random
from openai import OpenAI
from dotenv import load_dotenv
import os


class OpenAIRequestGenerator:
    random_topics = [
        "health",
        "career",
        "finance",
        "love",
        "family",
        "investments",
        "friendships",
        "opportunities",
    ]

    def __init__(self, model_name="gpt-4"):
        load_dotenv()
        self.client = OpenAI()
        self.client.api_key = os.getenv("OPENAI_API_KEY")
        self.model_name = model_name

    def choose_random_topic(self):
        """Choose a random value from the list."""
        return random.choice(self.random_topics)

    def generate_open_ai_completion(self, topic):
        """Generate OpenAI completion for a specific topic."""
        open_ai_completion_and_topic = {"completion": "", "topic": topic}

        stream = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Give a one-sentence new year about {topic} in a first person narrative",
                },
                {
                    "role": "assistant",
                    "content": "Be very practical and direct about expectations. Don't list categories. Your response should be conversational.",
                },
            ],
            stream=True,
        )

        # Capture responses in a list
        for chunk in stream:
            try:
                if chunk.choices[0].delta.content is not None:
                    open_ai_completion_and_topic["completion"] += chunk.choices[
                        0
                    ].delta.content
                    open_ai_completion_and_topic[
                        "completion"
                    ] = open_ai_completion_and_topic["completion"].replace("'", "")
            except Exception as e:
                print(f"Error occurred while processing chunk: {str(e)}")

        # Make sure the completion is not an empty string. If so, the chunk never assigned the content meaning an exception was thrown
        return (
            open_ai_completion_and_topic
            if len(open_ai_completion_and_topic["completion"]) > 0
            else {"error": "Empty completion"}
        )


# Example usage:
random_topics = [
    "health",
    "career",
    "finance",
    "love",
    "family",
    "investments",
    "friendships",
    "opportunities",
]
openai_request_generator = OpenAIRequestGenerator()

# Get a new random topic each time
random_topic = openai_request_generator.choose_random_topic()

# Generate OpenAI completion for the random topic
result = openai_request_generator.generate_open_ai_completion(random_topic)
