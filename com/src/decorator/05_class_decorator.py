# 装饰器实现类的静态方法
# 原地址：https://cloud.tencent.com/developer/article/1566268

class Myproperty():
    def __init__(self, fun):
        # print("执行Myproperty类的构造方法")   #调用Myproperty类时会首先运行它
        self.fun = fun

    def __get__(self, instance, owner):
        """
        :param instance: 代表school实例本身
        :param owner:  代表类School本身
        :return:
        """
        # print('调用Myproperty的属性时将执行此方法')
        return self.fun(instance)


class School():
    """
    @name:学校名字
    @addr:学校地址
    @price:学费
    @num:招生人数
    """

    def __init__(self, name, addr, price, num):
        self.name = name
        self.addr = addr
        self.price = price
        self.num = num

    # @property
    @Myproperty  # 等价于-->>total=Myproperty(total)
    def total(self):
        "求总的学费"
        return self.price * self.num


if __name__ == '__main__':
    school = School('浙江大学', '浙江省杭州市', 12000, 6000)
    print(school.total)  # 调用total方法时，会去调用Myproperty类的__get__方法
