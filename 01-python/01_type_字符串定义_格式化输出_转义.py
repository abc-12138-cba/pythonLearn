## 1. 使用变量接收 type() 返回的类型
result1 = type('张三')
result2 = type(18)
result3 = type(72.5)

print(result1) # <class 'str'> 注意此处返回的不是string，是 string 的简写：str
print(result2) # <class 'int'>
print(result3) # <class 'float'>


## 2. 字符串相关

# 2.1 字符串的定义
# 单引号和双引号的写法是等价的，二者都不能直接换行（要用圆括号才能换行），单引号用的多。
message1 = '你好!'
message2 = "你好!"

# 三个单引号的写法，可以直接换行，并且可以作为多行注释使用。
message3 = '''你好!'''

# 三个双引号的写法，可以直接换行，也可以作为多行注释使用，还能作为文档字符串使用。
message4 = """你好!"""

# 2.2 字符串格式化输出
name = '张三'
gender = '男'
weight = 65.2
age = 12

"""
  ● %s占位字符串
  ● %f占位浮点数
  ● %i占位整数
  ● %d占位十进制的整数
  ● %s是万能的（如果我们提供的数据不是字符串，那 Python 就会把数据转成字符串）。
"""
info2 = '我叫%s，我是%s生，我体重是%f，年龄是%d' % (name, gender, weight, age) # 占位符
print(info2)

""" f-string (推荐写法) """
name = '张三'
gender = '男'
weight = 65.2
age = 12

info3 = f'我叫{name}，我是{gender}生，我体重是{weight}，年龄是{age}'

print("在Python中，可以使用\"包裹一个字符串")
print("\"\"你好!\"\"")