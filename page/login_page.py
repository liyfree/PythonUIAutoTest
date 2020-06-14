#!/usr/bin/env python3
# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class LoginPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    login_btn = (By.XPATH, '//*[@id="loginForm"]/button')

    def input_username(self, text):
        self.send_key(self.username_loc, text)

    def input_password(self, text):
        self.send_key(self.password_loc, text)

    def click_login_btn(self):
        self.click(self.login_btn)
