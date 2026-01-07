"""
  None是一个特殊的字面量，它表示：空值 / 无值 / 无意义。
  None 的类型是 NoneType。
  不能参与数学运算，也不能与字符串拼接。
"""
print(type(None)) # NoneType
# print(None + '123') # 报错
# print(None + 22) # 报错


## global 关键字，把变量声明为全局变量
# a = 100

# def test():
#     global a  # 使用 global 关键字，将a声明为全局变量。
#     a = 300
#     print('函数中的打印（a）', a)
# test()
# print('全局的打印（a）', a)


## 函数说明文档：写在函数里的文字说明，用来描述：函数的功能、需要哪些参数、返回什么结果，它的语法和普通字符串一样，用三引号包裹
def add(n1, n2):
    """
    计算两个数相加的结果
    :param n1:第一个数
    :param n2:第二个数
    :return:二者相加的结果
    """
    return n1 + n2

result = add(1, 2) # 鼠标移到add有说明文档弹出