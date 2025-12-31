# 字典：用来存放一组『键值对』数据，可通过『键(key)』对『值(value)』进行：增、删、改、查操作

"""
  操作：
    1. 增加：字典[key] = 值
    2. 删除：
      del 字典[key]
      字典.pop([key], 默认值):  删除指定key所对应的那组键值对，并返回这个key所对应的值，如果key不存在，则报错。但可以传入第二个参数作为默认值返回，避免报错
      字典.clear(): 清空字典
    3. 修改
      字典[key] ： 值：key存在则修改，不存在则是新增
      字典.update({ key1: value1, key2: value2 }): 批量修改
    4. 查询
      字典[key]: 直接取值，key不存在则报错
      字典.get(key, 默认值): 取值，key不存在则返回默认值，避免报错

  常用方法
    1. 字典.keys(): 获取所有的key，返回一个可迭代对象，类型是 dict_keys ，不能通过下标访问元素，但可以通过list()函数转换成列表
    2. 字典.values(): 获取所有的value，返回一个可迭代对象，类型是 dict_values ，它的特点和dict_keys一样
    3. 字典.items(): 获取所有的键值对，返回一个可迭代对象，类型是 dict_items ，里面的每个元素都是一个元组，元组的第一个元素是key，第二个元素是value
"""


## 1. 定义
d1 = {'张三': 72, '李四': 60, '王五': 85}
print(type(d1), d1) # <class 'dict'> {'张三': 72, '李四': 60, '王五': 85}

# pop方法可以设置默认值
# 默认值可以保证：当要删除的key不存在的情况下，程序不会报错，并且返回这个默认值
result = d1.pop('奥特曼', '删除失败！') # 不传 删除失败！ 程序会报错
print(d1)
print(result)

result = d1.keys()
print(result) # dict_keys(['张三', '李四', '王五'])
print(type(result)) # <class 'dict_keys'>：dict_keys和列表类似，可以被遍历，但要注意的是：它不能通过下标访问元素
# 借助内置的list函数，可以将dict_keys转换成list
l1 = list(result)
print(l1)
print(type(l1))

result = d1.items()
print(result)
print(type(result))