import time
import unittest

from tests.test_base import TestBase
from resource.users_base import *


class TestLoginPage(TestBase):

    def test1_submit_button_enabled(self):
        self.login_page.login = 'admin'
        self.login_page.password = '1234'
        self.assertTrue(self.login_page.submit.is_enabled())

    def test2_sign_in_as_admin(self):
        self.login_page.login = 'admin'
        self.login_page.password = '1234'
        self.login_page.submit.click()
        time.sleep(2)
        self.assertEqual(self.driver.title, 'Caesar')

    def test3_sign_in_as_coordinator(self):
        self.login_page.login = 'dmytro'
        self.login_page.password = '1234'
        self.login_page.submit.click()
        time.sleep(2)
        self.assertEqual(self.driver.title, 'Caesar')

    def test4_sign_in_as_teacher(self):
        self.login_page.login = 'sasha'
        self.login_page.password = '1234'
        self.login_page.submit.click()
        time.sleep(2)
        self.assertEqual(self.driver.title, 'Caesar')

    def test5_length_password_equal_10(self):
        """

        Need to create user with login: vasya and password: 1234567890

        """
        self.login_page.login = 'vasya'
        self.login_page.password = '1234567890'
        self.login_page.submit.click()
        time.sleep(2)
        self.assertEqual(self.driver.title, 'Caesar')

    def test6_length_password_equal_4(self):
        self.login_page.login = 'dmytro'
        self.login_page.password = '1234'
        self.login_page.submit.click()
        time.sleep(2)
        self.assertEqual(self.driver.title, 'Caesar')

    def test_auto_login(self):
        first_admin.auto_login(self.login_page)
        self.assertEqual(self.driver.title, 'Caesar')

    # negative tests
    def test7_submit_button_disable(self):
        for step in range(3):
            if step == 0:
                self.login_page.login = 'admin'
                self.login_page.password.clear()
            elif step == 1:
                self.login_page.login.clear()
                self.login_page.password = '1234'
            elif step == 2:
                self.login_page.login.clear()
                self.login_page.password.clear()
            self.assertFalse(self.login_page.submit.is_enabled())

    def test8_length_password_equal_3(self):
        self.login_page.login = 'vasya2'
        self.login_page.password = '123'
        self.login_page.submit.click()
        self.assertEqual(self.login_page.massage.text, 'Incorrect login or password. Please, try again')

    def test9_length_password_equal_11(self):
        self.login_page.login = 'vasya1'
        self.login_page.password = '12345678901'
        self.login_page.submit.click()
        self.assertEqual(self.login_page.massage.text, 'Incorrect login or password. Please, try again')


if __name__ == '__main__':
    unittest.main()
