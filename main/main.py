#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

from util.case_util import TestCase


def get_case_files():
    """
    获取测试用例目录下的所有文件
    :return:
    """
    dir_path = "../case"
    file_list = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    file_list = filter(lambda item: "__init__" not in item, file_list)
    file_list = filter(lambda item: not item.endswith("pyc"), file_list)
    return file_list


case_files = get_case_files()
for case_f in case_files:
    # 加载测试用例模块
    case_module = __import__("case.{0}".format(os.path.splitext(case_f)[0]), fromlist=["*"])
    # 遍历用例模块下的所有函数
    for name, fn in case_module.__dict__.iteritems():
        # 如果函数使用了 @TestCase 注解， 则执行函数调用
        if isinstance(fn, TestCase):
            fn()

# 打印测试统计结果
TestCase.print_statistic_result()
