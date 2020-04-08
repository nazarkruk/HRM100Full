#######################################################################################################################
#                           HERE IS HOW TO CREATE TEST SUITES IN JUNIT
#######################################################################################################################

'''

1. Create Python Package "TestSuites" or with any other name
2. Import Classes from all tests witch need to be at the suite

(Example)

import unittest

from tests.login_test import LoginTestCase
from tests.personal_details_test import PersonalDetailsTestCase
from tests.contact_details_test import ContactDetailsTestCase
from tests.add_photograph_test import AddPhotoTestCase
from tests.emergency_contacts_test import EmergencyContactsTestCase

3. Load tests from test cases as bellow

ltc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase)
mitc1 = unittest.TestLoader().loadTestsFromTestCase(PersonalDetailsTestCase)
mitc2 = unittest.TestLoader().loadTestsFromTestCase(AddPhotoTestCase)
mitc3 = unittest.TestLoader().loadTestsFromTestCase(ContactDetailsTestCase)
mitc4 = unittest.TestLoader().loadTestsFromTestCase(EmergencyContactsTestCase)

4. Include all needed test cases to masterTestSuite

masterTestSuite = unittest.TestSuite([ltc1, mitc1, mitc2, mitc3, mitc4])

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)

5. Run TestSute as usual TestCases

'''