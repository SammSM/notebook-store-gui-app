from abc import ABC, abstractmethod

class AdminDAO(ABC):
    @abstractmethod
    def get_admin(self, username):
        pass

    @abstractmethod
    def verify_admin(self, username, password):
        pass

    @abstractmethod
    def add_admin(self, username, password_hash):
        pass
