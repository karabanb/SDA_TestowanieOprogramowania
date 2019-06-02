import unittest
import random


class FirstTest(unittest.TestCase):

    def setUp(self) -> None:
        self.imie = "Bartek"
        self.licbza = random.randint(1, 100)
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test1(self):
        self.assertEqual("Bartek", self.imie)
        self.assertEqual(1, self.licbza)
        print("test1")

    def test2(self):
        self.assertEqual("Bartlomiej", self.imie)
        self.assertEqual(2, self.licbza)
        print("test2")
