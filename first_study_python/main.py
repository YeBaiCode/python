# 缩进很重要
# if 5 > 2:
#     print("Hello World")

# x = 5
# y = "bai"
# print(x, y)
# x, y, z = 1, "2", 6
# print(x + y)

# x = "awesome"

# def myfunc():
#     print("Python is " + x)

# myfunc()

x = "awesome"
# 引用global使x变成全局变量
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

