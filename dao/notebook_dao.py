from abc import ABC, abstractmethod
from model.notebook import Notebook

class NotebookDAO(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_all_brands(self):
        pass

    @abstractmethod
    def get_all_os(self):
        pass

    @abstractmethod
    def get_all_types(self):
        pass

    @abstractmethod
    def add(self, notebook: Notebook):
        pass

    @abstractmethod
    def update(self, notebook: Notebook):
        pass

    @abstractmethod
    def delete(self, notebook_id: int):
        pass
