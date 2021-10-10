
'''while True:
    a = input()
    if a.count(".")>1:
        print("不是合法数字")
    elif a.isdigit():
        print("是整数")
    elif a == "0":
        break
    else :
        print("小数")'''

# b=(input("b:"))
# c=b.replace(".","0")
#
# if (c.isdigit()==True) and (b.count(".")==1):
#     print("b是小数")
# elif b.isdigit():
#     print("整数")
# else:


# flo1=input("请输入小数")   #证明小数形式的字符串转换为浮点型时保留位数的情况
# flo2=float(flo1)
# print(flo2)

# xi=input("小数")       # 判断字符的最后一位是不是小数点
# yi=len(xi)-1           #判断字符长度
# zi=xi[len(xi)-1]  #获取最后一位
# m1=xi[0]
# print(zi)
# print(m1)

# kf=pow(4,1/2)  #开方
# print(kf)

# tri=['t1','t2','t3']
# rec=[1,2,3,5]
# print(tri)
# print(rec)
count=2
a=4
tri=[1,2,3]
tri[count - 1] = float(a)
print(tri)