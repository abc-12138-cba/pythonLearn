# 函数

"""
  参数
    1. 位置参数,行参入参一一对应，『位置参数』必须写在『关键字参数』之前
    2. 关键字参数：不受顺序限制
    3. 限制传参方式: /前面只能用『位置参数』，*后面只能用『关键字参数』
    4. 参数默认值:『默认参数』必须放在『必选参数』的后面
    5. 可变参数: 
"""


# 定义函数
def greet(name, gender, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')

# 调用函数（使用关键字参数，不受定义顺序限制）
greet(name='张三', gender='男', age=18, height=172)
greet(height=172, age = 18, gender='男', name='张三')


## 限制传参方式：/前面只能用『位置参数』，*后面只能用『关键字参数』
# 定义函数（使用/和*限制传参方式）
def greet(name, /, gender, *, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')

# 正确示例
greet('张三', '男', age=18, height=172)
greet('张三', gender='男', age=18, height=172)

# 错误示例
# greet(name='张三', gender='男', age=18, height=172)
# greet('张三', '男', 18, height=172)


## 可变参数: 不确定会传入多少个参数，那就可以使用可变参数
#   使用 *形参名 来接收任意数量的『位置参数』，多个位置参数最终会被打包成一个『元组』
#   使用 **形参名 来接收任意数量的『关键字参数』，多个关键字参数最终会被打包成一个『字典』
# 定义函数（使用*args去接收：可变位置参数，args只是大家习惯这么写，当然也可以换成其他变量）
def test1(*args):
    print(args) # ('张三', '男', 18, 172)
# 调用函数
test1('张三', '男', 18, 172)


# 定义函数（使用**kwargs去接收：可变关键字参数，kwargs只是大家习惯这么写，当然也可以换成其他变量）
def test2(**kwargs):
    print(kwargs) # {'name': '张三', 'gender': '男', 'age': 18, 'height': 172}
# 调用函数
test2(name='张三', gender='男', age=18, height=172)

# 『可变位置参数』和『可变关键字参数』，同时使用，但必须要先写『可变位置参数』
# 定义函数（同时使用：可变位置参数、可变关键字参数）
def test3(a, b, *args, c='尚硅谷', **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
# 调用函数
test3('张三', '男', '抽烟', '喝酒', age=18, height=172)