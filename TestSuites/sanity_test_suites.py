import unittest

from tests.login_test import LoginTestCase


ltc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase)


sanityTestSuite = unittest.TestSuite([ltc1])

unittest.TextTestRunner(verbosity=2).run(sanityTestSuite)