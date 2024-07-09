
def fun_1(x):
    def fun_2(y):
        return x + y

    # 外部函数的返回值为闭包
    return fun_2


def logging(fn):
    def inner(num1, num2):
        print("--计算中--")
        result = fn(num1, num2)
        return result
    return inner


def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


# 装饰器
@makebold
@makeitalic
def hello():
    return "hello world"


@logging
def sum_num(a, b):
    result = a + b
    return result


def func_out(num1):

    def func_inner(num2):
        # 这里本意想要修改外部num1的值，实际上是在内部函数定义了一个局部变量num1
        nonlocal num1  # 声明是使用了外部变量
        # 内部函数使用了外部函数的变量(num1)
        result = num1 + num2
        print("结果是:", result)

    print(num1)
    func_inner(1)
    print(num1)

    # 外部函数返回了内部函数，这里返回的内部函数就是闭包
    return func_inner


if __name__ == '__main__':

    # 闭包
    # add = fun_1(8)
    # ret = add(5)
    # print(ret)
    #
    # # 装饰器测试
    # print(hello())
    #
    # # 创建闭包实例
    # f = func_out(1)
    # # 执行闭包
    # f(2)

    # 日志装饰器
    print(sum_num(1, 3))

