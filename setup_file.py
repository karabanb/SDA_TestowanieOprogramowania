import random
import unittest


def setUpModule():
    print("Uruchomione przed modulem")


def tearDownModule():
    print("Uruchomione po module")


class NewClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.liczba_wlasciwa = random.randint(1, 100)

    def setUp(self) -> None:
        self.liczba = random.randint(1, 100)

    def tearDown(self) -> None:
        print(self.liczba)
        self.liczba = None
        print(self.liczba)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.liczba_wlasciwa = None

    def test_1(self):
        self.assertEqual(self.liczba_wlasciwa, self.liczba)

    def test_2(self):
        self.assertEqual(self.liczba_wlasciwa, self.liczba)


class NewestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.liczba_wlasciwa = random.randint(1, 100)

    def setUp(self) -> None:
        self.liczba = random.randint(1, 100)

    def tearDown(self) -> None:
        print(self.liczba)
        self.liczba = None
        print(self.liczba)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.liczba_wlasciwa = None

    def test_1(self):
        self.assertEqual(self.liczba_wlasciwa, self.liczba)

    def test_2(self):
        self.assertEqual(self.liczba_wlasciwa, self.liczba)