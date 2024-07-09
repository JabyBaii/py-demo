import time


def func_out(func):
    def func_in():
        start = time.time()
        func()
        end = time.time()

        take_time = end - start
        print("共耗时：", take_time)
    return func_in


@func_out
def any_fun():
    for i in range(10000):
        print(i)


any_fun()

