from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def configure_worker(self, api_key, model, model_kwargs):
        ...

    @abstractmethod
    def generate_content(self, prompt):
        ...
