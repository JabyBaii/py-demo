"""
类装饰器
"""


class Func:
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        print("验证功能")
        self.__fn()


@Func
def my_fun():
    print("登录功能")


my_fun()

