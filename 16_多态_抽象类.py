# 多态：多种形态，同一个方法名，在不同的对象上调用时，能呈现出不同的行为
# Python中支持：标准多态、鸭子多态

"""
  多态
    标准多态
    鸭子多态:鸭子类型是一种编程风格，它不检查对象的类型，只关注对象能否“做某件事”（是否有对应的方法）

  抽象类 @abstractmethod ：是一种 不能被直接实例化 的类，通常作为“规范”，让子类去继承并实现其中定义的抽象方法，本身只定义规范，不需要提供完整实现
"""

# 标准多态：
class Animal:
    def speak(self):
        print('动物正在发出声音')

class Dog(Animal):
    def speak(self):
        print('汪汪汪！')

class Cat(Animal):
    def speak(self):
        print('喵喵喵！')

# 注意Pig类没有继承Animal类
class Pig:
    def speak(self):
        print('哼哼哼！')

# make_sound函数要求：传入的对象，必须是 Animal 类型（或其子类型），才能保证可以调用到sepak方法
def make_sound(animal:Animal):
    animal.speak()

# 创建实例对象
a1 = Animal()
d1 = Dog()
c1 = Cat()

# 多态的体现：同一函数，不同对象 → 不同行为
make_sound(a1)  # 动物正在发出声音
make_sound(d1)  # 汪汪汪！
make_sound(c1)  # 喵喵喵！

# 按标准多态规则：Pig 没有继承 Animal，类型不匹配（会出现类型警告）
p1 = Pig()
make_sound(p1)  # 在其它语言中会报错，虽然 Python 中能运行，但这不属于标准多态



# 鸭子多态
class Dog:
    def speak(self):
        print('汪汪汪！')

class Cat:
    def speak(self):
        print('喵喵喵！')

class Pig:
    def speak(self):
        print('哼哼哼！')

class Fish:
    def speak(self):
        print('咕噜噜！')

# 不再对animal的类型做限制，animal可以是任何类型，只要能调用speak方法就可以
def make_sound(animal):
    animal.speak()

# 创建实例对象
d1 = Dog()
c1 = Cat()
p1 = Pig()
f1 = Fish()

make_sound(d1)
make_sound(c1)
make_sound(p1)
make_sound(f1)


## 抽象类
from abc import ABC, abstractmethod

#【抽象类】是一种不能直接实例化的类，它通常作为“规范”，让子类去继承，并实现其中定义的【抽象方法】。

# MustRun类一旦继承了ABC类，那MustRun类就是【抽象类】了
class MustRun(ABC):
    # run方法一旦被@abstractmethod装饰后，就变成了【抽象方法】
    @abstractmethod
    def run(self):
        pass

class Person(MustRun):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print(f'我叫{self.name}，我在努力的奔跑！')

p1 = Person('张三', 18, '男')
p1.run()