#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time:2020/6/12 21:20
# @Author:李阳
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class BaiduPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """

    input_loc = (By.ID, 'kw')
    search_btn_loc = (By.ID, 'su')

    def input_text(self, text):
        self.send_key(self.input_loc, text)

    def click_search_btn(self):
        self.click(self.search_btn_loc)
