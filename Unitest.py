
import unittest

class FirstTest(unittest.TestCase):


class SecondTest(unittest.TestCase):

    def test_01_succes(self):
        print("01")
        self.assertEqual(2, 2)

    def test_02_failure(self):
        print("02")
        self.assertEqual(2, 3)
