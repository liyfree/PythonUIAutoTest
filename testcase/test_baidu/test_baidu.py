#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time:2020/6/12 21:19
# @Author:李阳
import unittest
from page.baidu_page import BaiduPage
from common.browser import BrowserDriver


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = BrowserDriver()
        cls.page = BaiduPage(cls.browser.get_driver())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit_browser()

    def test_baidu(self):
        self.page.input_text('Python')
        self.page.click_search_btn()
        self.assertEqual('python', self.page.get_title())
