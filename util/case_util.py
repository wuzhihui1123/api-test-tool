# coding=utf-8

import time

from termcolor import *


class TestCase(object):
    test_case_list = []
    test_file_list = []
    case_success_list = []
    case_fail_list = []

    def __init__(self, fn):
        case_path = TestCase.get_case_path(fn)
        arg_count = fn.func_code.co_argcount
        if arg_count > 0:
            raise Exception("测试用例函数不能有参数，{0} 含有 {1} 个参数".format(case_path, arg_count))
        TestCase.test_case_list.append(case_path)
        file_name = TestCase.get_case_file_name(fn)
        if file_name not in TestCase.test_file_list:
            TestCase.test_file_list.append(file_name)
        self.fn = fn

    def __call__(self):
        case_path = TestCase.get_case_path(self.fn)
        try:
            result = self.fn()
            TestCase.case_success_list.append(case_path)
            print colored("======> √ Assert ok , case_path: [ {0} ]".format(case_path), "blue")
            return result
        except AssertionError as e:
            # traceback.print_exc()
            print colored("======> × Assert Fail, case_path: {0}, Info: [ {1} ]".format(case_path, e.message), "red")
            TestCase.case_fail_list.append(case_path)

    @classmethod
    def print_cases(cls):
        print cls.test_case_list

    @classmethod
    def print_statistic_result(cls):
        """
        打印统计结果
        :return:
        """
        time.sleep(0.05)  # 睡眠一小段时间，以免与某些trace信息混合打印
        test_file_count = len(cls.test_file_list)
        case_success_count = len(cls.case_success_list)
        case_fail_count = len(cls.case_fail_list)
        out_str = "\n"
        out_str += "=============== 测试结果统计======================\n" + \
                   "执行文件数：{0}\n".format(test_file_count) + \
                   "case总 数：{0}\n".format(case_success_count + case_fail_count) + \
                   "case成功数：{0}\n".format(case_success_count) + \
                   "case失败数：{0}".format(case_fail_count);
        if case_fail_count > 0:
            out_str += "   =>"
            for case_name in cls.case_fail_list:
                out_str = out_str + " {0},".format(case_name)
            out_str = out_str[:-1]

        out_str += "\n"
        out_str += "=================================================\n"
        print out_str

    @classmethod
    def get_case_path(cls, fn):
        return cls.get_case_file_name(fn) + "/" + fn.__name__

    @classmethod
    def get_case_file_name(cls, fn):
        return os.path.basename(fn.func_code.co_filename)
