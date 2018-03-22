import time
import unittest

from tests.test_base import TestBase
from resource.users_base import *
from front.pages.groups_page import GroupsPage


class TestLoginPage(TestBase):

    def test1_submit_button_enabled(self):
        self.login_page.login = 'admin'
        self.login_page.password = '1234'
        self.assertTrue(self.login_page.submit.is_enabled())

    def test2_sign_in_as_admin(self):
        self.login_page.login = first_admin.login
        self.login_page.password = first_admin.password
        self.login_page.submit.click()
        time.sleep(1)
        self.assertEqual(self.driver.title, 'Caesar')
        group_page = GroupsPage(self.driver)
        self.assertEqual(group_page.group_location.text, first_admin.location)
        group_page.user_photo.click()
        self.assertEqual(group_page.user_full_name.text, first_admin.full_name)
        self.assertEqual(group_page.user_role.text, 'ITA ' + first_admin.role)

    def test3_sign_in_as_coordinator(self):
        self.login_page.login = coordinator.login
        self.login_page.password = coordinator.password
        self.login_page.submit.click()
        time.sleep(1)
        self.assertEqual(self.driver.title, 'Caesar')
        group_page = GroupsPage(self.driver)
        self.assertEqual(group_page.group_location.text, coordinator.location)
        group_page.user_photo.click()
        self.assertEqual(group_page.user_full_name.text, coordinator.full_name)
        self.assertEqual(group_page.user_role.text, 'ITA ' + coordinator.role)

    def test4_sign_in_as_teacher(self):
        self.login_page.login = teacher.login
        self.login_page.password = teacher.password
        self.login_page.submit.click()
        time.sleep(1)
        self.assertEqual(self.driver.title, 'Caesar')
        group_page = GroupsPage(self.driver)
        self.assertEqual(group_page.group_location.text, teacher.location)
        group_page.user_photo.click()
        self.assertEqual(group_page.user_full_name.text, teacher.full_name)
        self.assertEqual(group_page.user_role.text, 'ITA ' + teacher.role)

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
