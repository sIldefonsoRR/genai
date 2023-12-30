from workers.gemini import Gemini_worker
from dotenv import load_dotenv
import os


gemini_prompt = 'Tell me a riddle about'


def call_google_gemini_example(gemini_prompt):
    # get configurations
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    model_name = 'gemini-pro'

    # start the worker
    worker = Gemini_worker()
    worker.configure_worker(api_key, model_name)

    # ask the model
    response = worker.generate_content(gemini_prompt)

    # retrieve the answer
    print(response)


call_google_gemini_example(gemini_prompt)
