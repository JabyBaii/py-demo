
def func_out(func):
    def func_in(*args, **kwargs):
        func(*args, **kwargs)

    return func_in


@func_out
def any_fun(*args, **kwargs):
    print(args)
    print(kwargs)


any_fun(10, 23, age=20)

