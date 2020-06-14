#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time:2020/6/14 08:28
# @Author:李阳
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class UserManagePage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    user_manage_loc = (By.XPATH, '//*[@id="admui-navTabsItem-32"]/ul/li[2]/a')
    user_manage_add_loc = (By.XPATH, '//*[@id="admui-navTabsItem-32"]/ul/li[2]/ul/li[2]')
    add_student_loc = (By.XPATH, '//*[@id="admui-pageContent"]/div[1]/div[1]/div/div/button')
    stu_name_loc = (By.XPATH, '//*[@id="stuName"]')
    stu_sex_loc = (By.CSS_SELECTOR, '#add-update-form > div:nth-child(3) > div > div')

    stu_class_loc = (By.XPATH, '//*[@id="add-update-form"]/div[4]/div/select')
    stu_city_loc = (By.XPATH, '//*[@id="add-update-form"]/div[5]/div/div/select')
    stu_school_loc = (By.XPATH, '//*[@id="add-update-form"]/div[6]/div/select')
    stu_graduate_loc = (By.XPATH, '//*[@id="graduateDate"]')
    stu_contact_loc = (By.XPATH, '//*[@id="add-update-form"]/div[9]/div/input')
    stu_contact_class_loc = (By.XPATH, '//*[@id="add-update-form"]/div[10]/div/select')
    stu_contact_phone_loc = (By.XPATH, '//*[@id="add-update-form"]/div[11]/div/input')
    save_btn_loc = (By.XPATH, '//*[@id="submit-btn"]')

    search_condition_loc = (By.XPATH, '//*[@id="admui-pageContent"]/div[1]/div[1]/div/button')

    search_name_loc = (By.XPATH, '//*[@id="adviser-leader-student-form"]/div[1]/input')
    search_phone_loc = (By.XPATH, '//*[@id="adviser-leader-student-form"]/div[2]/input')

    search_btn_loc = (By.XPATH, '//*[@id="adviser-leader-student-form"]/div[3]/button[1]')

    table_name_loc = (By.XPATH, '//*[@id="student-list-table"]/tbody/tr/td[1]')
    table_phone_loc = (By.XPATH, '//*[@id="student-list-table"]/tbody/tr/td[7]')

    def _click_usermanage(self):
        self.click(self.user_manage_loc)

    def click_usermanage_add(self):
        self._expand_menu()
        self.click(self.user_manage_add_loc)

    def _expand_menu(self):
        js = """
            $("#admui-navTabsItem-32 > ul > li.site-menu-item.has-sub").addClass("open");
            """
        self.js_execute(js)

    def _coll_menu(self):
        js2 = """
            $("#admui-navTabsItem-32 > ul > li.site-menu-item.has-sub").removeClass("open");
            """
        self.js_execute(js2)

    def click_add_stu(self):
        self.click(self.add_student_loc)

    def input_stu_name(self, name):
        self.send_key(self.stu_name_loc, name)

    def select_stu_sex(self, sex):
        index = 1 if sex == '男' else 2
        js = f"$('input[type=\"radio\"][value=\"{index}\"]').attr('checked', 'true')"
        self.js_execute(js)

    def select_stu_class(self, text):
        self.select_by_text(self.stu_class_loc, text)

    def select_study_city(self, city):
        self.select_by_text(self.stu_city_loc, city)

    def select_study_school(self, school):
        self.select_by_text(self.stu_school_loc, school)

    def select_graduate_date(self, date):
        self.send_key(self.stu_graduate_loc, date)

    def input_contact(self, name):
        self.send_key(self.stu_contact_loc, name)

    def select_contact_class(self, text):
        self.select_by_text(self.stu_contact_class_loc, text)

    def input_contact_phone(self, phone):
        self.send_key(self.stu_contact_phone_loc, phone)

    def save(self):
        self.click(self.save_btn_loc)

    def click_search_condition(self):
        self.click(self.search_condition_loc)

    def input_search_name(self, name):
        self.send_key(self.search_name_loc, name)

    def input_search_phone(self, phone):
        self.send_key(self.search_phone_loc, phone)

    def search(self):
        self.click(self.search_btn_loc)

    def get_search_result_name(self, name, phone):
        self.input_search_name(name)
        self.input_search_phone(phone)
        self.search()
        return self.get_text(self.table_name_loc)
