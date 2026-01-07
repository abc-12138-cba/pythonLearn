# 『对象』是一个拥有『属性』和『行为』的个体

# _类属性与实例属性_实例方法_类方法_静态方法
"""
  类定义
    属性
      实例属性访问：
        对象.属性名 
        对象.__dict__： 查看对象身上的所有属性
      实例属性增加：
        对象.属性名 = 值，__dict__ 就增加了这个属性

    行为：是绑在类上的函数，而不是实例对象

  实例属性与类属性

  实例方法、类方法、静态方法
    实例方法：保存在类身上，并且主要是通过实例调用 （实例和类都可直接调用，但类调用不推荐）
    类方法：使用 @classmethod 装饰器修饰，第一个参数是类本身，通常用形参cls接收。（类方法，也能通过实例调用到，但是非常不推荐）
    静态方法：使用 @staticmethod 装饰器修饰，方法没有self或cls参数，只是单纯的定义在类中。
"""


# 定义一个Person类（类名通常使用：大驼峰写法）
class Person:
    # 说明：当一个函数被定义在了类中时，那这个函数就被称为：方法。
    # __init__方法：初始化方法，主要作用：给当前正在创建的实例对象添加属性
    # __init__方法收到的参数：当前正在创建的实例对象（self）、其它的自定义参数
    # 当我们以后编写代码去创建Person类实例的时候，Python会自动调用__init__方法
    def __init__(self, name, age, gender):
        # 给实例添加属性（语法为：self.属性名 = 值）
        self.name = name
        self.age = age
        self.gender = gender

# 创建Person的实例对象
p1 = Person('张三', 18, '男')
print(p1) # 直接打印一个实例的话，我们是看不到实例身上的属性的
# 通过点语法可以访问或修改实例身上的属性
print(p1.name)
print(p1.age)
print(p1.gender)

# 通过 实例.__dict__ 可以查看实例身上的所有属性
print(p1.__dict__)

# 实例创建完毕后，依然可以通过 实例.属性名 = 值 去给实例追加属性
p1.address = '北京昌平宏福科技园'
print(p1.__dict__)

# 通过type函数，可以查看某个实例对象，是由哪个类创建出来的
print(type(p1))


## 行为
# 定义一个Person类
class Person:
    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 自定义方法（给实例添加行为）
    # speak方法收到的参数是：调用speak方法的实例对象（self）、其它参数
    # speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用到speak方法
    def speak(self, msg = '默认msg'):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

# speak方法是存在Person类身上的
print(Person.__dict__)

# 创建Person类的实例对象
p1 = Person('张三', 18, '男')

# 当执行p1.speak()的时候，查找speak方法的过程：1.实例对象自身(p1)  =>  2.实例的“缔造者”的身上(Person)
# 验证一下上述的查找过程
def speak():
    print('巴拉巴拉巴拉巴拉巴拉')
# p1.speak = speak
print(p1.__dict__)
p1.speak()


## 实例属性、类属性
# 实例属性：通过实例.属性名 = 值定义在实例身上的属性
# 定义一个Person类
class Person:
    # max_age、planet 他们都是类属性，类属性是保存在类身上的
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存：公共数据
    max_age = 120
    planet = '地球'

    # 初始化方法
    def __init__(self, name, age, gender):
        # 给实例添加属性
        self.name = name
        self.gender = gender



## 实例方法、类方法、静态方法
# 定义一个Person类
class Person:
    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 下面的speak方法、run方法，都保存在类身上，但他们主要是供实例调用，所以他们都叫：实例方法
    # 自定义方法（给实例添加行为）
    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

    # 自定义方法（给实例添加行为）
    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

p1 = Person('张三', 18, '男')
Person.run(p1, 100)

## 类方法
# 定义一个Person类
class Person:
    # 类属性
    max_age = 120
    planet = '地球'

    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # speak方法、run方法，他们都属于：实例方法
    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

    # 使用 @classmethod 装饰过的方法，就叫：类方法，类方法保存在类身上的
    # 类方法收到的参数：当前类本身（cls）、自定义的参数
    # 因为收到了cls参数，所以类方法中是可以访问类属性的
    # 类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息、一些工厂方法
    @classmethod
    def change_planet(cls, value):
        cls.planet = value
print(Person.__dict__)
