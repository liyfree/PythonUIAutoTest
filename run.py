#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os
import sys
import time
import unittest

from report.HTMLTestRunner3 import HTMLTestRunner


def report():
    """
    生成测试报告
    :return:
    """
    if len(sys.argv) > 1:
        report_name = os.path.dirname(os.getcwd()) + '\\report\\' + sys.argv[1] + '_test_report.html'
        print(report_name)
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        # 需要查看每段时间的测试报告，可以这样写：
        # report_name = os.getcwd() + '\\report\\'+now+'result.html'
        report_name = './report/test_report.html'
        print(f'报告名称{report_name}')
        return report_name


def create_suite():
    suit = unittest.TestSuite()  # 测试集
    test_dir = 'testcase/test_gwzz'  # 测试用例文件夹

    discover = unittest.defaultTestLoader.discover(  # 搜索测试用例
        start_dir=test_dir,
        pattern='test*.py',
        top_level_dir=None
    )

    for test_case in discover:  # 遍历测量用例加入测试集
        suit.addTests(test_case)
    return suit


if __name__ == '__main__':
    suit = create_suite()

    with open(report(), 'wb') as fp:
        Runner = HTMLTestRunner(
            stream=fp,
            title='测试报告',
            description='测试用例执行情况'
        )
        Runner.run(suit)

