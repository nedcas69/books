from django.test import TestCase
from logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 25, '+')
        self.assertEqual(31, result)
    def test_minus(self):
        result = operations(6, 25, '-')
        self.assertEqual(-19, result)
    def test_multiply(self):
        result = operations(6, 25, '*')
        self.assertEqual(31, result)
