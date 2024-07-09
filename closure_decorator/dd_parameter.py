"""
装饰器带参数
"""


def logging(flag):
    def func_out(func):
        def func_in(num1, num2):
            if flag == "+":
                print("执行加法")
            elif flag == "-":
                print("执行减法")
            result = func(num1, num2)
            return result

        return func_in

    return func_out


@logging('+')
def add(a, b):
    result = a + b
    return result


@logging('-')
def sub(a, b):
    result = a - b
    return result


print(add(1, 3))
print(sub(1, 3))
