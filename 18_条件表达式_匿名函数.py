"""
  条件表达式：结果1 if 条件 else 结果2

  匿名函数：lambda 参数: 表达式（当一个函数只用一次、只做一点点小事，使用匿名函数会更简洁）

"""

age = 20
## 条件表达式写法
text = '成年' if age >= 18 else '未成年·'
print(text)


## 使用匿名函数实现计算效果
def calculate(func, a, b):
    print(f'计算结果为：{func(a, b)}')

calculate(lambda x, y: x + y, 30, 10)
calculate(lambda x, y: x - y, 30, 10)


## 匿名函数 + 条件表达式
is_adult = lambda age: '成年' if age >= 18 else '未成年'
print(is_adult(18))
print(is_adult(13))