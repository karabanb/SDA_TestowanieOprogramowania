import unittest


class SecondTest(unittest.TestCase):

    def test01_succes(self):
        print("01")
        self.assertEqual(2, 2)

    def test_02_failure(self):
        print("02")
        self.assertEqual(2, 3)

    def testc_failure(self):
        print("02")
        self.assertEqual(2, 3)

class ThirdTest(unittest.TestCase):

    def aTest_succes(self):
        print("01")
        self.assertEqual(2, 2)

    def test02_failure(self):
        print("02")
        self.assertEqual(2, 3)

    def Testfailure(self):
        print("02")
        self.assertEqual(2, 3)

if __name__ == '__main__':
    unittest.main()