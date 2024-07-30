from abc import ABC, abstractmethod


class Command(ABC):

    def get_command(self):
        return self.command

    @abstractmethod
    def execute(self):
        pass
