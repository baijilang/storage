#使用random模块，如何产生 50~150之间的数？
'''
优化：
    1.可以自己选择范围
    2.可以选择保留的小数位数
    3.可多次使用，输入q退出停止
'''
###################################################
import random
while True:
    L = input("输入边界1：")
    F = input("输入边界2：")
    U = input("输入小数位数：")
    if L.isdigit() and F.isdigit() and U.isdigit():
        while True:
            start=input("点击回车开始，点击q停止：")
            if start=="":
                ran=random.uniform(int(L),int(F))
                if ran>float(int(F)):
                    ran=ran-int(F)
                    ran=round(ran,int(U))
                    print(ran)
                else:
                    ran = round(ran,int(U))
                    print(ran)
            elif start=="q":
                break
            else:
                continue
    elif L=="q" or F=="q" or U=="q":
        break
    else:
        print("输入有误")
