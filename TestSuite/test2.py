import unittest

from TestSuite.test1 import TestForSuite


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestForSuite)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
