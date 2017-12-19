# coding=utf-8


def verify(actual, **argv):
    if len(argv) is not 0:
        __assert_not_equal(len(actual), 0)
    for (k, v) in argv.items():
        __assert_equal(actual[k], v)


def __assert_equal(lhs, rhs, errmsg=None):
    """
    @summary: 断言lhs和rhs相等
    @param errmsg: 断言失败时显示的信息
    """
    if errmsg is None:
        errmsg = "%s doesn't equal to: %s" % (lhs, rhs)

    if lhs != rhs:
        raise AssertionError(errmsg)


def __assert_not_equal(lhs, rhs, errmsg=None):
    """
    @summary: 断言lhs和rhs不想等
    @param errmsg: 断言失败时显示的信息
    """
    if errmsg is None:
        errmsg = "%s equals to: %s" % (lhs, rhs)

    if lhs == rhs:
        raise AssertionError(errmsg)


def __assert_true(expr, msg=None):
    """
    Fail the test unless the expression is true.
    """
    if not expr: raise AssertionError, msg


def __assert_false(expr, msg=None):
    """
    Fail the test if the expression is true.
    """
    if expr:
        raise AssertionError(msg)


def __assert_gt(lhs, rhs, errmsg=None):
    """
    @summary: 断言lhs大于rhs
    @param errmsg: 断言失败时显示的信息
    """
    if errmsg is None:
        errmsg = "%s is less than or equal to %s" % (lhs, rhs)

    if lhs <= rhs:
        raise AssertionError(errmsg)


def __assert_bound(value, lb, hb, errmsg=None):
    """
    @summary: 断言value介于lb和hb之间，包含边界
    @param errmsg: 断言失败时显示的信息
    @param lb: 下限
    @param hb: 上限
    """
    if errmsg is None:
        errmsg = "%s is not in [%s, %s]" % (value, lb, hb)

    if value < lb or value > hb:
        raise AssertionError(errmsg)


def __assert_in_list(ele, lis, errmsg=None):
    """
    @summary: 断言element是list中的一个元素
    """
    if errmsg is None:
        errmsg = "%s is not in %s" % (ele, lis)

    if ele not in lis:
        raise AssertionError(errmsg)


def __assert_contains(lhs, rhs, errmsg=None):
    if errmsg is None:
        errmsg = "%s not in: %s" % (rhs, lhs)

    if type(lhs) != type(rhs):
        raise AssertionError("format not matched")
    if not rhs:
        print "%s is Empty" % rhs
        return
    if isinstance(lhs, dict):
        for k, v in rhs.items():
            print k, v
            if k not in lhs:
                raise AssertionError("%s not in: %s" % (k, lhs))
            elif lhs[k] == v:
                continue
            else:
                raise AssertionError(errmsg)
    elif isinstance(lhs, list):
        for item in rhs:
            if item not in lhs:
                raise AssertionError(errmsg)
            else:
                continue
    elif isinstance(lhs, str):
        str_l = lhs.split(',')
        str_r = rhs.split(',')
        __assert_contains(str_l, str_r)


def __assert_not_haskey(lhs, rhs, errmsg=None):
    """
    assert if lhs.has_key(rhs)
    """
    if errmsg is None:
        errmsg = "%s not in %s" % (rhs, lhs)
    if not isinstance(lhs, dict):
        errmsg = "%s is not a dict" % (lhs)
        raise AssertionError(errmsg)
    if lhs.has_key(rhs):
        raise AssertionError(errmsg)
