import pickle

# list1=float(input("in:"))
# # list2=list1.split(",")
# a=[1,2,3,4]
# a1="xy"
# b="1.2."
# c=b.replace(".","1")
# print(c)
# d=b.count(".")
# print(d)
# a1b=a1+b
# print(list1)
# print(a1b)
# print(float("-12"))
# print(len(a))

# list1=input("输入数字,逗号隔开：")
# list=list1.split(",")
# print(list[4])

# from ctypes import *
# user32= windll.LoadLibrary("user32.dll")

# 控制锁屏
# from ctypes import *
# user32 = windll.LoadLibrary('user32.dll')
# user32.LockWorkStation()

a=int(input("输入高度："))
b=input("输入符号：")
c=input("输入填充符：")
for i in range(1,a+1):
    b1=[b]*i
    b2=' '.join(b1)
    b3=b2.center(9*a,c)
    print(b3)
for i in range(1,a+1):
    b1=[b]*(a+1-i)
    b2=' '.join(b1)
    b3=b2.center(9*a,c)
    print(b3)