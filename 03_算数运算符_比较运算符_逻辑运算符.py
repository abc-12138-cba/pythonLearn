## 1. 算数运算符：常见的：加减乘除等
# 取整: 向下取整
print(9 // 6) # 1


## 2. 比较运算符：主要根据 Unicode 做比较
# 使用ord()查看指定字符的Unicode编码
print(ord('a')) # 97 
print(ord('我')) # 25105 

# 使用chr()将Unicode编码转为字符
# print(chr(97))
# print(chr(25105))

msg1 = 'abc'
msg3 = '我爱你'
print(msg3 <= msg1)

a = True
print(type(a), a) # <class 'bool'> True


## 3. 逻辑运算符：and、or、not