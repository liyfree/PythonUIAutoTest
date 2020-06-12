#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os
import sys
import time
import unittest
from report.HTMLTestRunner3 import HTMLTestRunner


def create_suite():
    suit = unittest.TestSuite()  # 测试集
    test_dir = 'testcase'

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='test*.py',
        top_level_dir=None
    )

    for test_case in discover:
        suit.addTests(test_case)
    return suit


def report():
    if len(sys.argv) > 1:
        report_name = os.path.dirname(os.getcwd()) + '\\report\\' + sys.argv[1] + '_result.html'
        print(report_name)
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        # 需要查看每段时间的测试报告，可以这样写：
        # report_name = os.getcwd() + '\\report\\'+now+'result.html'
        report_name = './report/result.html'
        print(f'报告名称{report_name}')
    return report_name


if __name__ == '__main__':
    suit = create_suite()
    fp = open(report(), 'wb')
    Runner = HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='测试用例执行情况'
    )
    Runner.run(suit)
    fp.close()
