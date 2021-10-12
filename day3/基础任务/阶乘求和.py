'''
输入20以内的正整数可以进行计算所有小于或等于输入数字的阶乘之和
输入q退出
输入非整数或超过超过限制的数字报错
'''

while True:
    num=input("输入正整数：")
    Fac=1
    Sum=0
    if num.isdigit() and int(num)<=20:
        num=int(num)
        for i in range(1,num+1):
            if i<=num+1:
                Fac*=i
                Sum+=Fac
        print(Sum)
    elif num=="q":
        break
    else:print("输入有误")



