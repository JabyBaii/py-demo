def make_bold(fn):
    print("in func01_out")

    def wrapped_bold():
        print("in func01_in")
        return "<b>" + fn() + "</b>"
    return wrapped_bold


def make_italic(fn):
    print("in func02_out")

    def wrapped_italic():
        print("in func02_in")
        return "<i>" + fn() + "</i>"

    return wrapped_italic


@make_bold
@make_italic
def hello():
    return "hello world"


print(hello())

