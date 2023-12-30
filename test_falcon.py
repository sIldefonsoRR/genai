from workers.falcon import Falcon_Worker
from dotenv import load_dotenv
import os


falcon_prompt = 'What is Portugal?'


def call_falcon_example(falcon_prompt):
    # get configurations
    load_dotenv()
    api_key = os.environ['HUGGINGFACEHUB_API_TOKEN']
    model_name = "tiiuae/falcon-7b"
    model_kwargs = {"temperature": 0.1, "max_new_tokens": 2000}

    # start the worker
    worker = Falcon_Worker()
    worker.configure_worker(api_key, model_name, model_kwargs)

    # ask the model
    response = worker.generate_content(falcon_prompt)

    # retrieve the answer
    print(response)


call_falcon_example(falcon_prompt)
