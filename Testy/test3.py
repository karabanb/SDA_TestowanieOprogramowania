import unittest

from Testy import test1 as test

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loaded_test = loader.loadTestsFromTestCase(test.TestForSuite)
    loaded_module = loader.loadTestsFromModule(test)
    loaded_test2 = loader.loadTestsFromTestCase(test.TestForSuite)
    loaded_module2 = loader.loadTestsFromModule(test)
    suite.addTest(loaded_test)
    suite.addTest(loaded_module)
    suite.addTests([loaded_test2, loaded_module2])
    # suite.addTests([loader.loadTestsFromModule(), loader.loadTestsFromTestCase()])
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite())
