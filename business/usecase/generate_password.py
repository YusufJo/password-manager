import secrets
import uuid

from business.model.password import Password
from business.usecase.use_case_abstract import UseCase
from business.util.generator_config import GeneratorConfig


class GeneratePassword(UseCase):
    __config: GeneratorConfig

    def __init__(self, generator_config: GeneratorConfig):
        self.__config = generator_config

    def __call__(self, title: str) -> Password:
        uid = str(uuid.uuid4())
        pass_elements = [element for sublist in self.__config.c_type_styles() for element in sublist]
        pass_phrase = ''.join(
            secrets.SystemRandom().choice(pass_elements) for i in range(self.__config.length))
        return Password(uid=uid, title=title, pass_phrase=pass_phrase)
