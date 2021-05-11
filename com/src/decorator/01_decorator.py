import functools


# 无参的装饰器
def log(func):
    @functools.wraps(func)  # 把原函数的元消息拷贝到装饰器里的func里
    def wrapper(*args, **kwargs):
        print('call %s()' % func.__name__)  # 由于前面装饰器，__name__保留了func原本的名字，即test
        print('args = {}'.format(*args))
        return func(*args, **kwargs)

    return wrapper


# 入参的装饰器：有三层函数
def log_with_param(text):  # 最外层形参为装饰器参数
    def decorator(func):  # 第二层形参为被修饰函数
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s()' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log
def test(p):
    print(test.__name__ + 'params: ' + p)


@log_with_param(text='text')
def test_with_param(p):
    print(test_with_param.__name__ + 'params: ' + p)


if __name__ == '__main__':
    test("I'm a param")
    # 效果与以下调用方式等价:
    # wrapper = log(test)
    # wrapper("I'm a param")

    test_with_param('abc')
    # 效果与以下调用方式等价:
    # decorator = log_with_param('text')
    # wrapper = decorator(test_with_param)
    # wrapper('abc')
