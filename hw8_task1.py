def wrapper_with_func_name(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"{func.__name__} will return {res}")
        return res

    return wrapper


@wrapper_with_func_name
def add_two_numbers(a, b):
    return a + b


@wrapper_with_func_name
def multipl_two_numbers(x, y):
    return x * y


if __name__ == '__main__':
    add_two_numbers(4, 5)
    multipl_two_numbers(5, 4)

