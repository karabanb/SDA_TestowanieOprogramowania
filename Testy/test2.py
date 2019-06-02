import unittest

from Testy.test1 import TestForSuite


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestForSuite('test_for_suite'))
    suite.addTest(TestForSuite('test_for_suite_new'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
