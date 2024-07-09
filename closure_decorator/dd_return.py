
def func_out(func):
    def func_in(*args, **kwargs):
        _ret = func(*args, **kwargs)

        return _ret

    return func_in


@func_out
def any_fun(*args, **kwargs):
    print(args)
    print(kwargs)

    return 100


ret = any_fun(10, 23, age=20)
print(ret)

