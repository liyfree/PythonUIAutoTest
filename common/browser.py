#!/usr/bin/env python3
# -*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.utils.config import Config
from common.utils.logger import Logger

logger = Logger(logger="BrowserDriver").getlog()


class BrowserDriver(object):
    """
    驱动类，封装driver设置信息，返回
    """
    # path = './drivers/'  # 这是获取相对路径的方法
    # chrome_driver_path = path + 'chromedriver.exe'
    # firfox_driver_path = path + 'chromedriver.exe'
    # ie_driver_path = path + 'IEDriverServer.exe'

    def __init__(self):
        self.driver = None
        self.config = Config()
        self.browser_name = self.config.get('browser').get('name')  # 从配置文件读取浏览器名称
        self.driver_path = self.config.get('browser').get('driver_path')  # 从配置文件读取driver地址
        logger.info(f"选择的浏览器为: {self.browser_name}浏览器")
        url = self.config.get('URL')  # 从配置文件读取访问地址
        logger.info(f"打开的URL为: {url}")

        if self.browser_name == "Firefox":
            self.driver = webdriver.Firefox(executable_path=self.driver_path)
            logger.info("启动火狐浏览器")
        elif self.browser_name == "Chrome":
            chrome_options = Options()
            chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
            chrome_options.add_argument('--start-maximized')  # 指定浏览器分辨率
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('lang=zh_CN.UTF-8')
            self.driver = webdriver.Chrome(options=chrome_options, executable_path=self.driver_path)
            logger.info("启动谷歌浏览器")
        elif self.browser_name == "IE":
            self.driver = webdriver.Ie(executable_path=self.driver_path)
            logger.info("启动IE浏览器")

        self.driver.get(url)
        # logger.info("打开URL: %s" % url)
        self.driver.maximize_window()
        logger.info("全屏当前窗口")
        self.driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")

    def get_driver(self):
        return self.driver

    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()
