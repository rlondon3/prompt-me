from chat_gpt.openai_completions import ai_resolution


class Chat_GPT_Handler:
    def get_completion():
        try:
            response = ai_resolution()
            if response:
                return response
        except Exception as e:
            # Handle exceptions and return an error message
            return {"handler error": [str(e)]}, 400
        
def chat_gpt_route(app):
    app.add_url_rule("/resolution", "show_resolution", Chat_GPT_Handler.get_completion, methods=["GET"])
    
    