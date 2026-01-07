# 继承：指一个类，可以继承另一个类的属性和方法

"""
  继承方式：
    先声明，在继承：Student(Person)
    1. super().__init__(name, age, gender)
    2. Person.__init__(self, name, age, gender)

  isinstance() 和 issubclass()
    isinstance(obj, Class)：判断对象是否为指定类或其子类的**实例**
    issubclass(Sub, Super)：判断一个类是否是另一个类的**子类**

  多重继承
"""
# 定义一个Person类
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

# 定义一个Student类（子类、派生类）， 继承自Person类（父类、超类、基类）
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        # 在子类中，有两种方式去调用父类的初始化方法，来实现对继承属性：name, age, gender 初始化操作
        # 方式1（更推荐）
        super().__init__(name, age, gender)

        # 方式2
        # Person.__init__(self, name, age, gender)

        # 子类独有的属性，需要自己手动完成初始化
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f'我叫{self.name}，我在努力的学习，争取做到{self.grade}年级的第一名')

# 创建Student类的实例对象
s1 = Student('李华', 16, '男', '2025001', '初二')
print(s1.__dict__)


# 方法重写：当子类中定义了一个与父类中相同的方法，那么子类中的方法就会“覆盖”父类的方法


# 所谓多重继承，就是一个类，可以同时继承多个父类
# 定义一个Person类
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}')

# 定义一个Worker类
class Worker:
    def __init__(self, company):
        self.company = company
    def do_work(self):
        print(f'我在{self.company}做兼职')

# 定义一个Student类，继承自：Person类、Worker类
class Student(Person, Worker):
    def __init__(self, name, age, gender, stu_id, grade, company):
        Person.__init__(self, name, age, gender)
        Worker.__init__(self, company)
        self.stu_id = stu_id
        self.grade = grade
    def study(self):
        print(f'我在很努力的学习，争取做{self.grade}年级的第一名')

# 创建Student实例对象
s1 = Student('张三', 18, '男', '2025001', '初二', '麦当劳')
print(s1.__dict__)
s1.speak()
s1.do_work()
s1.study()

# 类的__mro__属性：用于记录属性和方法的查找顺序
# 通过实例去查找属性或方法时，会现在实例自身上寻找，如果没有，就按照__mro__中所记录的顺序去查找
print(Student.__mro__)