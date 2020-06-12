#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os
from common.utils.readFile import YamlReader

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_FILE = os.path.join(BASE_PATH, 'data', 'browser.yaml')


# ELEMENT_PATH = os.path.join(BASE_PATH,'data','elements.yaml')
# CASE_PATH = os.path.join(BASE_PATH,'data','testcase.yaml')
# INTERFACE_PATH = os.path.join(BASE_PATH,'data','interface.yaml')
# DATA_PATH = os.path.join(BASE_PATH, 'data')
# DRIVER_PATH = os.path.join(BASE_PATH, 'drivers','chromedriver.exe')
# LOG_PATH = os.path.join(BASE_PATH, 'logs')
# REPORT_PATH = os.path.join(BASE_PATH, 'report')
# SCREENSHOTS_PATH = os.path.join(BASE_PATH,"screenshots",'')
# EXE_PATH = os.path.join(BASE_PATH,'test','Autolt','test1.jpg')
# EXCEL_PATH = os.path.join(BASE_PATH,'test','configSQL','')

# ,element = ELEMENT_PATH,case_data = CASE_PATH,
#                  interface_data = INTERFACE_PATH,chrome = DRIVER_PATH,screenshot = SCREENSHOTS_PATH,
#                  excel = EXCEL_PATH
class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)

