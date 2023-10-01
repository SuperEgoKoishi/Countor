def count_calls(func):
    count = 0

    def add_count(is_display=False):
        func()
        nonlocal count
        if is_display:
            print("The function has been executed {} time(s)".format(count))
        else:
            count += 1

    return add_count


@count_calls
def target_func():
    print("Execute target function...")


if __name__ == '__main__':
    for i in range(114514):
        target_func()
    target_func(is_display=True)
