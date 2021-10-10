'''
需要手动输入三条边长
判断是否可以生成三角形以及三角形的面积
'''

import math
print("=========三角形计算========\n输入回车或q退出")
count=1
tri=[1,2,3]
while True:
    if count<4:
        a=input("输入第%d个数:"%(count))
        a1=a.count(".")
        if a!="":
            a2=a[0]
        else:
            break
        a3=a[len(a)-1]
        a4=a.replace(".","1")
        if ((a.isdigit())or((a1==1) and (a2!=".") and (a3!=".") and (a4.isdigit()) ) )and (count < 4):
            tri[count-1] = float(a)
            count=count+1
        elif a == "q":
            break
        else:
            print("输入非法")
    elif count>=4:
        ptri=tri[0]
        qtri=tri[1]
        rtri=tri[2]
        if ((ptri+qtri)>rtri) and ((ptri+rtri)>qtri) and ((rtri+qtri)>ptri):
            p=(tri[0]+tri[1]+tri[2])/2
            Stri=pow(p*(p-tri[0])*(p-tri[1])*(p-tri[2]),1/2)
            print("可以生成三角形\n三角形的面积为:%.2f"%(Stri))
            count=1
        else :
            print("不能生成三角形")
            count=1



