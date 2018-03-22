from front.pages.base_page import BasePage
from page_objects import PageObject, PageElement
from selenium import webdriver


class GroupsPage(PageObject, BasePage):
    user_photo = PageElement(class_name='user-photo')
    top_menu = PageElement(id_='top-menu')
    right_menu = PageElement(id_='right-menu')
    left_menu = PageElement(id_='left-menu')
    group_location = PageElement(class_name='groupLocation')

    # top menu elements
    top_menu_logout = PageElement(css='#top-menu > div.logout > a > i')
    top_menu_locations = PageElement(css='#top-menu > div.containerMainMenu > div:nth-child(1)')
    top_menu_groups = PageElement(css='#top-menu > div.containerMainMenu > div:nth-child(2)')
    top_menu_students = PageElement(css='#top-menu > div.containerMainMenu > div:nth-child(3)')
    top_menu_schedule = PageElement(css='#top-menu > div.containerMainMenu > div:nth-child(4)')
    top_menu_add = PageElement(css='#top-menu > div.containerMainMenu > div:nth-child(5)')
    top_menu_about = PageElement(css='#top-menu > div.containerMainMenu > div:nth-child(6)')

    # right menu elements
    right_menu_logout = PageElement(css='#right-menu > div > a > i')
    user_full_name = PageElement(class_name='name')
    user_role = PageElement(class_name='role')
    edit_user_button = PageElement(css='#right-menu > div > button > i')

    # left menu elements
    create_button = PageElement(css='#left-menu > div > div:nth-child(1) > button > i')
    search_button = PageElement(css='#left-menu > div > div:nth-child(2) > button > i')


class CreateGroup(PageObject):
    group_name = PageElement(name='name')


class Directions(CreateGroup):
    web_ui = PageElement(css='#modal-window > section > section > section'
                             ' > div:nth-child(3) > div:nth-child(1) > select > option:nth-child(2)')
    java_script = PageElement(css='#modal-window > section > section > section '
                                  '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(3)')
    lamp = PageElement(css='#modal-window > section > section > section '
                           '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(4)')
    dot_net = PageElement(css='#modal-window > section > section > section '
                              '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(5)')
    ios = PageElement(css='#modal-window > section > section > section '
                          '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(6)')
    c_plus_plus = PageElement(css='#modal-window > section > section > section '
                                  '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(7)')
    delphi = PageElement(css='#modal-window > section > section > section '
                             '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(8)')
    java = PageElement(css='#modal-window > section > section > section '
                           '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(9)')
    rdbms = PageElement(css='#modal-window > section > section > section '
                            '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(10)')
    mqc = PageElement(css='#modal-window > section > section > section '
                          '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(11)')
    atqc = PageElement(css='#modal-window > section > section > section '
                           '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(12)')
    istqb = PageElement(css='#modal-window > section > section > section '
                            '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(13)')
    dev_ops = PageElement(css='#modal-window > section > section > section '
                              '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(14)')
    ux = PageElement(css='#modal-window > section > section > section '
                         '> div:nth-child(3) > div:nth-child(1) > select > option:nth-child(15)')
