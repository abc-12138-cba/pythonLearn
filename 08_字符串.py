"""
  字符串（str）：用来存放一组有序的字符数据，但其中的内容不可修改（只能查，不能增删改）

  常用方法：
    字符串.index(字符)：指定字符第一次出现的下标
    字符串.split(字符)：按照『指定字符』进行分隔，返回值：列表
    字符串.replace(字符串片段): 将字符串中的某个字符串片段，替换成目标字符串
    字符串.count(字符): 统计『指定字符』在字符串中出现的次数，返回值：下标
    字符串.strip(): 从某个字符串中删除指定字符串中的任意字符，不会修改原字符串，返回值：新字符串
      规则：从字符串两端开始删除，直到遇到第一个不在字符串中的字符就停下

  常用内置函数: max、min、len、sorted、sum函数
"""

# 字符串中的字符，不可修改
msg = 'welcome to atguigu'
# msg[0] = 'a' # 报错

msg  = '尚硅谷@atguigu@你好'
result = msg.split('@')
print(msg, result)  # 尚硅谷@atguigu@你好 | ['尚硅谷', 'atguigu', '你好']

msg = 'welcome to atguigu'
result = msg.replace('atguigu', '尚硅谷')
print(msg)    # welcome to atguigu
print(result) # welcome to 尚硅谷

msg = '666尚6硅6谷666'
result = msg.strip('6')
print(msg)    # 666尚6硅6谷666
print(result) # 尚6硅6谷