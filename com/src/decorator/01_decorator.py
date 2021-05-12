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


# 类装饰器
def class_decorator(obj):  # print(School.__dict__)
    # 添加对象属性
    obj.param = 'param'

    def print_param():
        pass

    # 添加对象方法
    obj.func = print_param
    return obj


# 带参类装饰器：给类添加一个可变的数据属性(类属性)
def class_decorator_with_param(**kwargs):
    def add(obj):
        for key, value in kwargs.items():
            setattr(obj, key, value)
        return obj
    return add

@log
def test(p):
    print(test.__name__ + 'params: ' + p)


@log_with_param(text='text')
def test_with_param(p):
    print(test_with_param.__name__ + 'params: ' + p)


# 类装饰器调用
@class_decorator
class TestClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 带参类装饰器调用
@class_decorator_with_param(sex='male', city='shanghai')
class Person:
    def __init__(self):
        self.name = 'sqw'
        self.age = 100


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

    # 打印类的属性字典
    print(TestClass.__dict__)  # 显示'param': 'param': 'func': <function class_decorator.<locals>print_param ...

    print(Person.__dict__)
    # 检查装饰器新增的属性是否为类属性
    p1 = Person()
    p2 = Person()
    print(p1.sex)
    print(p2.sex)
    Person.sex = 'female'
    print(p1.sex)
    print(p2.sex)   # p1,p2的sex转为female，说明sex属性是类属性
