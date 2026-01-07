"""
  数据处理函数
    map: map(操作函数, 可迭代对象)
    filter: filter(过滤函数, 可迭代对象)
    sorted: sorted(可迭代对象, key=xxx, reverse=xxx)
    reduce: reduce(合并函数, 可迭代对象, 初始值) -- (reduce函数需要从functools模块中引入才能使用)
  
  列表推导式：用一条简洁语句，从可迭代对象中，生成新列表的语法结构
    [ 表达式 for 变量 in 可迭代对象 ]
    类比：字典推导式、集合推导式

  常见内置函数

  浅拷贝、深拷贝
    import copy -- copy.copy -- copy.deepcopy
"""


# 统一数据处理
nums = [10, 20, 30, 40]
# map函数的返回值是一个迭代器对象，需要我们自己去手动遍历，或者手动类型转换
result = map(lambda x: x * 2, nums)
print(list(result)) # [20, 40, 60, 80]
print(nums) # [10, 20, 30, 40]


# 筛选数值
nums = [10, 20, 30, 40, 50]
result = filter(lambda n: n > 30, nums)
print(list(result))
print(nums)

# 数字排序
nums = [30, 40, 20, 10]
result = sorted(nums, reverse=True)
print(result)

# 按照字符串的长度去排序
names = ['python', 'sql', 'java']
result = sorted(names, key=len, reverse=True)
print(result)

# 根据字典中的某个字段进行排序
persons = [
    {'name':'张三', 'age':15, 'gender':'男'},
    {'name':'李四', 'age':17, 'gender':'女'},
    {'name':'王五', 'age':19, 'gender':'男'},
    {'name':'李华', 'age':20, 'gender':'女'},
    {'name':'赵六', 'age':18, 'gender':'女'},
    {'name':'孙七', 'age':16, 'gender':'男'}
]
result = sorted(persons, key=lambda p: p['age'], reverse=True)
print(result)


# 从 functools 模块中引入 reduce
from functools import reduce

# 数值统计
nums = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, nums, 10)
print(result)

nums = [10, 20, 30, 40]
result = [n * 2 for n in nums]
print(result)

# 带条件的列表推导式
nums = [10, 20, 30, 40]
result = [n * 2 for n in nums if n > 20] # 让nums列表中所有满足条件的元素，都变为原来的2倍
print(result)



import copy
## 浅拷贝
nums1 = [10, 20, 30, 40]
nums2 = copy.copy(nums1)
nums2[3] = 99

print(nums1[3]) # 40
print(nums2[3]) # 99

# 深拷贝
nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.deepcopy(nums1)
nums2[3][0] = 99

print(nums1[3][0])
print(nums2[3][0])