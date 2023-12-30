from .base import BaseWorker
import google.generativeai as genai


class Gemini_worker(BaseWorker):
    def __init__(self) -> None:
        ...

    def configure_worker(self, api_key, model, model_kwargs):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name=model)

    def generate_content(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
