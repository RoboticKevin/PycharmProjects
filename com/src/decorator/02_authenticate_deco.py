# 装饰器实现身份认证


import functools


# 身份验证的装饰器
# 用于装饰需要身份验证的函数，如评论、购买等
def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        # 如果用户处于登录状态
        if check_user_logged_in(request):
            # 执行函数 post_comment()
            return func(*args, **kwargs)
        else:
            raise Exception('Authentication failed')

    return wrapper


# 评论功能
@authenticate
def post_comment(request):
    print('用户{}新增评论{}'.format(request['user'], request['comment']))


# 检查用户是否登录
def check_user_logged_in(request):
    return 'user' in request and request['user'] is not None and len(request['user']) != 0


if __name__ == '__main__':
    request1 = {'user': 'shaoqiwen', 'comment': 'helloworld'}
    request2 = {'user': None, 'comment': 'helloworld'}
    try:
        post_comment(request1)
        post_comment(request2)
    except Exception:
        pass
