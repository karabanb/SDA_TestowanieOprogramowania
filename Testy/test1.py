import unittest


class TestForSuite(unittest.TestCase):

    def test_for_suite(self):
        self.assertEqual("a", "a")

    def test_for_suite_new(self):
        self.assertIsInstance("text", str)

