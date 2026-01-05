def beauty(char, n):
    def show_msg(msg):
        print(char * n + msg + char * n)
    return show_msg

show1 = beauty('*', 3)
show1('你好啊')
show1('尚硅谷')