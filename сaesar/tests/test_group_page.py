from tests.test_base import TestBase
from resource.users_base import *
from front.pages.groups_page import GroupsPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGroupPage(TestBase):

    def test1_logout_right_menu(self):
        """
        This test check logout at the right menu
        actions:
        1. login as user
        2. click user photo(right menu appears)
        3. check user name
        4. click logout button
        """
        first_admin.auto_login(self.login_page)
        group_page = GroupsPage(self.driver)
        group_page.user_photo.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of(group_page.right_menu_logout))
        group_page.right_menu_logout.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of(self.login_page.login))
        self.assertEqual(self.driver.title, 'Log in - Caesar')

    def test2_logout_top_menu(self):
        """
        This test check logout at the right menu
        actions:
        1. login as user
        2. move cursor at the top of page(top menu appears)
        3. click logout button
        """
        first_admin.auto_login(self.login_page)
        group_page = GroupsPage(self.driver)
        move_mouse_to_hover = ActionChains(self.driver).move_to_element(group_page.top_menu)
        move_mouse_to_hover.perform()
        WebDriverWait(self.driver, 3).until(EC.visibility_of(group_page.top_menu_logout))
        group_page.top_menu_logout.click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of(self.login_page.login))
        self.assertEqual(self.driver.title, 'Log in - Caesar')


