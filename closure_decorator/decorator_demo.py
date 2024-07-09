"""
decorator: 在不修改原有函数代码的情况下，给函数增加新的功能
"""


def func_out(func):
    def func_in():
        print("00 验证功能")
        func()

    return func_in


@func_out
def login():
    print("01 登录功能")


login()

