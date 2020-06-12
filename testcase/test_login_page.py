#!/usr/bin/env python3
# -*-coding:utf-8-*-
import unittest
from ddt import ddt, data
from common.browser import BrowserDriver
from common.utils import readFile
from common.utils.logger import Logger
from page.login_page import BaiduPage

logger = Logger('TestLoginPage').getlog()

# 读取测试用例到列表
case_list = readFile.ExcelReader('data/logincase.xlsx', sheet=0, title_line=True).data
# logger.info(f'读取测试用例excel：{case_list}')


@ddt
class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserDriver()  # 初始化浏览器对象
        cls.page = BaiduPage(cls.browser.get_driver())

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit_browser()

    @data(*case_list)  # 加载测试数据
    def test_login(self, data):
        logger.info(data)
        self.page.input_username(data['username'])
        self.page.input_password(data['password'])
        self.page.click_login_btn()
        self.assertEqual(data['check'], self.page.get_title())
