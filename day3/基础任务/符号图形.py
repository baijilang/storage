'''
1.使用 A='m'.join(list1)  可以将表格list转化为字符串，以字符m连接每个字符，m可以是空格
'''
###################################################
a=int(input("输入高度："))
b=input("输入符号：")
c=input("输入填充符：")
for i in range(1,a+1):
    b1=[b]*i
    b2=' '.join(b1)   #  使用 A='m'.join(list1)  可以将表格list转化为字符串，以字符m连接每个字符，m可以是空格
    b3=b2.center(2*a+1,c) #将b2按照2*a+1的长度居中排成一列，空的地方以"c"填充
    print(b3)
for i in range(2,a+1):
    b1=[b]*(a+1-i)
    b2=' '.join(b1)
    b3=b2.center(2*a+1,c)
    print(b3)