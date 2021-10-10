# 练习2：输入圆的半径计算计算周长和面积。
import math
r=input("请输入圆的半径(cm)：")
places=input("保留小数位数：")
R1=r.count(".")
R2=r[0]
if (r.isdigit())or(R1==1 and R2!="."):
    if r>0 and places>0:
        C=2*math.pi*r
        C1=round(C,places)
        S=math.pi*r*r
        S1=round(S,places)
        print("圆的周长是：",C1,"cm","面积是:",S1,"cm^2")
    elif r>0 and places==0:
        C=2*math.pi*r
        C1=int(C)
        S=math.pi*r*r
        S1=int(S)
        print("圆的周长是：",C1,"cm","面积是:",S1,"cm^2")
    elif r>0 and places<0:
        print("请输入正确小数位数")
    elif r<=0 and places>=0:
        print("r只能为正数")
    else:
        print("我看你是完全不懂哦")
else :
    print("输入非法")
