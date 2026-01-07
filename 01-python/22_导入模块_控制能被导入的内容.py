# 模块

"""
  导入模块
    1. 导入所有：import order --> order.create_order()
    2. 别名引入所有：import order as dd --> dd.create_order()
    3. 部分引入：from order import create_order, show_info  --> create_order()
    4. 部分引入加别名：from order import create_order as create_order22, show_info as show1  --> create_order22()
    5. 导入所有：from order import *  --> create_order()

  __all__  与  __name__
    1. __all__ 作用：控制 from 模块名 import * 导入的内容, 值可以是：列表、元组
    2. __name__ 作用：判断当前模块是被直接执行还是被导入执行: 主程序直接运行，__name__ 的值是 __main__；如果是被导入的模块，__name__ 的值是模块的名字,不带.py扩展名
"""