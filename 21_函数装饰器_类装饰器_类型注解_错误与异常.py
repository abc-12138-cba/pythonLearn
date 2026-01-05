# 装饰器：【不修改原函数代码】的前提下，对函数进行【增强】的工具，接收一个函数作为参数，并返回一个新函数

"""
_函数装饰器_类装饰器_类型注解_错误与异常__
  函数装饰器
    手动装饰
    @ 语法糖装饰
    带参数的函数装饰器(核心：最终是三层嵌套结构：外层接收配置、中间层接收函数、内层接收具体参数)
    多个函数装饰器一起使用: 距离函数最近的装饰器，会先工作
  类装饰器

  类型注解(ts)
    int、float、str、bool、list、tuple、dict、set

  错误与异常
    1. try：尝试去做可能会出现异常的事情。
    2. except：出现异常时的处理（出现异常时怎么补救）。
    3. else：如果一切顺利（没有异常出现）要做的事。
    4. finall：无论有没有异常，都要做的事。
    raise语句手动触发（抛出）异常
"""


# 需求：在不修改add函数的前提下，给add函数增加一些额外的功能，例如：计算前打印一句欢迎语。
# 手动装饰
def say_hello(func):
    def wrapper(*args, **kwargs):
        print('你好，我要开始计算了')
        return func(*args, **kwargs)
    return wrapper

def add(x, y, z):
    res = x + y + z
    print(f'{x}和{y}和{z}相加的结果是：{res}')
    return res

# 调用say_hello装饰器，对add函数进行装饰，并得到装饰后的新函数
add = say_hello(add)

result = add(10, 20, 30)
print(result)

# 语法糖 @
def say_hello(func):
    def wrapper(*args, **kwargs):
        print('你好，我要开始计算了')
        return func(*args, **kwargs)
    return wrapper

@say_hello
def add(x, y, z):
    res = x + y + z
    print(f'{x}和{y}和{z}相加的结果是：{res}')
    return res

result1 = add(10, 20, 30)
print(result1)


# 带参数的函数装饰器
def say_hello(msg):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(f'你好，我要开始{msg}计算了')
            return func(*args, **kwargs)
        return wrapper
    return outer

# 装饰加法函数
@say_hello('加法')
def add(x, y, z):
    res = x + y + z
    print(f'{x}和{y}和{z}相加的结果是：{res}')
    return res

# 装饰减法函数
@say_hello('减法')
def sub(x, y):
    res = x - y
    print(f'{x}和{y}相减的结果是：{res}')
    return res

# 测试代码
result1 = add(10, 21, 30)
print(result1)

print('-------------------')
# 多个函数装饰器一起使用
def test1(func):
    print('我是test1装饰器')
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('test1追加的逻辑')
        return res
    return wrapper

def test2(func):
    print('我是test2装饰器')
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('test2追加的逻辑')
        return res
    return wrapper

@test1
@test2
def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res

result = add(10, 20)
print(result)


## 类型注解

# hobby 是列表，并且列表中的元素，可以是：str 或 int 类型
hobby: list[str | int] = ['抽烟', '喝酒', '烫头']
# citys 是集合，并且集合中所有元素可以是：str 或 float 或 bool 类型
citys: set[str | float | bool] = {'北京', '上海', '深圳'}
# persons 是字典，键是 str 或 int 类型，值是 int 类型
persons: dict[str | int, int] = {'张三': 18, '李四': 19, '王五': 20}
# scores 是元组，并且元组中包含3个int类型的元素
scores: tuple[int, int, int] = (60, 70, 80)
# scores 是元组，并且元组中包含任意个数的元素，每个元素的类型可以是：int 或 str
scores: tuple[int | str, ...] = (60, '70', 80, '90', 100)