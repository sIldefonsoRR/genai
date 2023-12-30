from .base import BaseWorker
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os


class Falcon_Worker(BaseWorker):

    def configure_worker(self, api_key, model, model_kwargs):
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = api_key
        self.llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b",
                                  model_kwargs={"max_length": 100})
        self.template = """Question: {question}
Answer: """

    def generate_content(self, prompt):
        self.prompt = PromptTemplate(template=self.template,
                                     input_variables=["question"])
        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm)
        question = prompt
        output = self.llm_chain.run(question)
        return output
