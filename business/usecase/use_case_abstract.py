from abc import ABC, abstractmethod


class UseCase(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass
