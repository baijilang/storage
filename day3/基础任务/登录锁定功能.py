'''实现登陆系统的三次密码输入错误锁定功能
（用户名：root,密码：admin）'''
#####################################################
import time
Name="root"
Password="admin"
count=0
in_names="1"
in_password="1"
while True:
    if count<3 and in_names!="q":
        in_names=input("用户名：")
        in_password=input("密码：")
        count+=1
        if in_names==Name:
            if in_password==Password:
                count=0
                print("Welcome!")
                break
            else:
                print("密码错误")
        else:
            print("用户不存在")
    elif count<3 and (in_names=="q" or in_password=="q"):
        break
    else :
        count=0
        from ctypes import *
        user32= windll.LoadLibrary('user32.dll')
        user32.LockWorkStation()



