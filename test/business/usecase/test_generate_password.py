import unittest
import re

from business.usecase.generate_password import GeneratePassword
from business.usecase.use_case_abstract import UseCase
from business.util.generator_config import GeneratorConfig


class GeneratePasswordIsAUseCase(unittest.TestCase):
    def test_implements_UseCase(self):
        self.assertIsInstance(GeneratePassword(GeneratorConfig()), UseCase)


class GeneratePasswordObeysDefaultConfiguration(unittest.TestCase):
    sut_default: GeneratePassword

    @classmethod
    def setUpClass(cls) -> None:
        cls.sut_default = GeneratePassword(GeneratorConfig())

    def test_generated_password_has_uppercase_chars(self):
        self.assertTrue(re.search('[A-Z]', self.sut_default('website.com').pass_phrase))

    def test_generated_password_has_lowercase_letters(self):
        self.assertTrue(re.search('[a-z]', self.sut_default('website.ord').pass_phrase))

    def test_generated_password_has_digits(self):
        self.assertTrue(re.search('\\d', self.sut_default('mywebsite.dev').pass_phrase))

    def test_generated_password_has_punctuation(self):
        self.assertTrue(re.search('[@_!#$%^&*()<>?/|}{~:]', self.sut_default('other.com').pass_phrase))


if __name__ == '__main__':
    unittest.main()
