import unittest

from business.util.generator_config import GeneratorConfig


class TestGeneratorConfigAttrs(unittest.TestCase):
    sut: GeneratorConfig

    @classmethod
    def setUpClass(cls) -> None:
        cls.sut = GeneratorConfig()

    def test_has_length(self):
        self.assertEqual(hasattr(self.sut, 'length'), True)

    def test_has_allow_upper(self):
        self.assertEqual(hasattr(self.sut, 'allow_upper'), True)

    def test_has_allow_lower(self):
        self.assertEqual(hasattr(self.sut, 'allow_lower'), True)

    def test_has_allow_numeric(self):
        self.assertEqual(hasattr(self.sut, 'allow_numeric'), True)

    def test_has_allow_punct(self):
        self.assertEqual(hasattr(self.sut, 'allow_punct'), True)


class TestGeneratorConfigDefaults(unittest.TestCase):
    sut: GeneratorConfig

    @classmethod
    def setUpClass(cls) -> None:
        cls.sut = GeneratorConfig()

    def test_length_is_16(self):
        self.assertEqual(self.sut.length, 16)

    def test_upper_chars_allowed(self):
        self.assertTrue(self.sut.allow_upper)

    def test_lower_chars_allowed(self):
        self.assertTrue(self.sut.allow_lower)

    def test_numerics_allowed(self):
        self.assertTrue(self.sut.allow_numeric)

    def test_punctuation_allowed(self):
        self.assertTrue(self.sut.allow_punct)


class TestGeneratorConfigLength(unittest.TestCase):
    def test_less_than_4_raise_exception(self):
        self.assertRaises(Exception, lambda: GeneratorConfig(length=3))

    def test_greater_than_100_raise_exception(self):
        self.assertRaises(Exception, lambda: GeneratorConfig(length=101))


class TestGeneratorConfigLetterCase(unittest.TestCase):
    def test_disallowing_upper_AND_lower_raise_exception(self):
        self.assertRaises(Exception, lambda: GeneratorConfig(allow_upper=False, allow_lower=False))


if __name__ == '__main__':
    unittest.main()
