#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time:2020/6/14 08:24
# @Author:李阳
import unittest

import ddt

from common.browser import BrowserDriver
from common.utils import readFile
from page.gwzz_page.user_manage_page import UserManagePage
from page.login_page import LoginPage

cases = readFile.ExcelReader('data/gwzz_case.xlsx', sheet='用户管理', title_line=True).data


@ddt.ddt
class TestUserManage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = BrowserDriver()
        cls.page = LoginPage(cls.browser.get_driver())
        cls.page.input_username('lygwzz')
        cls.page.input_password('111111')
        cls.page.click_login_btn()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit_browser()

    @ddt.data(*cases)
    def test_add_student(self, data):
        stu_name = data.get('学生姓名', '')
        phone = data.get('联系人电话', '')
        page = UserManagePage(self.browser.get_driver())
        page.click_usermanage_add()
        page.click_add_stu()

        page.input_stu_name(stu_name)
        page.select_stu_sex(data.get('学生性别', ''))
        page.select_stu_class(data.get('学生类别', ''))
        page.select_study_city(data.get('就读城市', ''))
        page.select_study_school(data.get('就读学校', ''))
        # page.select_graduate_date(data.get('毕业时间', ''))
        page.input_contact(data.get('联系人姓名', ''))
        page.select_contact_class(data.get('联系人类别', ''))
        page.input_contact_phone(phone)
        page.save()

        page.click_search_condition()

        page.input_search_name(stu_name)
        page.input_search_phone(phone)
        page.search()
        self.assertEqual(data.get('检验条件'), page.get_search_result_name(stu_name, phone))
