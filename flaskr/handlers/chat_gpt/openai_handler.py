from flaskr.chat_gpt.openai_completions import OpenAIRequestGenerator


class Chat_GPT_Handler:
    @staticmethod
    def get_completion():
        try:
            # Create a new instance of OpenAIRequestGenerator for each request
            openai_request_generator = OpenAIRequestGenerator()

            # Get a new random topic each time
            random_topic = openai_request_generator.choose_random_topic()

            # Generate OpenAI completion for the random topic
            completion_result = openai_request_generator.generate_open_ai_completion(
                random_topic
            )

            return completion_result
        except Exception as e:
            # Handle exceptions and return an error message
            return {"handler error": [str(e)]}, 400


def chat_gpt_route(app):
    app.add_url_rule(
        "/resolution",
        "show_resolution",
        Chat_GPT_Handler.get_completion,
        methods=["GET"],
    )
