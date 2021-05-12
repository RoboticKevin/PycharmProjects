# 检查输入合法性

import functools


def validation_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pass  # 检查输入是否合法


@validation_check
def neural_network_training(param1, param2, *param):
    pass
