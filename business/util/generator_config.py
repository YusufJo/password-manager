import string
from typing import List


class GeneratorConfig:
    MIN_LENGTH = 16
    MAX_LENGTH = 100

    def __init__(self, length=16, allow_lower=True, allow_upper=True, allow_punct=True, allow_numeric=True):
        self.__validate_length(length)
        self.__validate_letter_case(allow_lower=allow_lower, allow_upper=allow_upper)

        self.length = length
        self.allow_lower = allow_lower
        self.allow_upper = allow_upper
        self.allow_punct = allow_punct
        self.allow_digits = allow_numeric

    def __validate_length(self, value: int) -> None:
        if value < self.MIN_LENGTH:
            raise Exception(f'password cannot be less than {self.MIN_LENGTH} characters long')
        if value > self.MAX_LENGTH:
            raise Exception(f'password cannot be greater than {self.MAX_LENGTH} characters long')

    @staticmethod
    def __validate_letter_case(allow_lower: bool, allow_upper: bool) -> None:
        if not allow_lower and not allow_upper:
            raise Exception('password must contain letters in upper-case, lower-case, or both')

    def c_type_styles(self) -> List[str]:
        result: List[str] = []
        if self.allow_upper:
            result.append(string.ascii_uppercase)
        if self.allow_lower:
            result.append(string.ascii_lowercase)
        if self.allow_punct:
            result.append(string.punctuation)
        if self.allow_digits:
            result.append(string.digits)
        return result
