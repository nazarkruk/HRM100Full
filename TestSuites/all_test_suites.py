import unittest

from tests.login_test import LoginTestCase
from tests.personal_details_test import PersonalDetailsTestCase
from tests.contact_details_test import  ContactDetailsTestCase
from tests.add_photograph_test import AddPhotoTestCase
from tests.emergency_contacts_test import EmergencyContactsTestCase


ltc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase)
mitc1 = unittest.TestLoader().loadTestsFromTestCase(PersonalDetailsTestCase)
mitc2 = unittest.TestLoader().loadTestsFromTestCase(AddPhotoTestCase)
mitc3 = unittest.TestLoader().loadTestsFromTestCase(ContactDetailsTestCase)
mitc4 = unittest.TestLoader().loadTestsFromTestCase(EmergencyContactsTestCase)

masterTestSuite = unittest.TestSuite([ltc1, mitc1, mitc2, mitc3, mitc4])

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)