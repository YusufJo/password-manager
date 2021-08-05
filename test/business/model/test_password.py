import copy
import unittest

from business.model.password import Password


class TestPasswordModel(unittest.TestCase):
    sut: Password

    @classmethod
    def setUpClass(cls):
        cls.sut = Password('unique_identifier', "website.com", "my_pass_phrase")

    def test_has_unique_id(self):
        self.assertEqual(hasattr(self.sut, 'uid'), True)

    def test_has_name(self):
        self.assertEqual(hasattr(self.sut, 'name'), True)

    def test_has_password(self):
        self.assertEqual(hasattr(self.sut, 'pass_phrase'), True)

    def test_two_equal_object_are_equal(self):
        other = copy.deepcopy(self.sut)
        self.assertEqual(self.sut, other)

    def test_two_NOT_equal_object_are_NOT_equal(self):
        other = Password("unique_identifier", "website.org", "my_pass_phrase")
        self.assertNotEqual(self.sut, other)


if __name__ == '__main__':
    unittest.main()
