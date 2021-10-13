# 这是一个示例 Python 脚本。
##test1
# a=[1,2,3,6,9]  sort的用法
# b=a.sort(reverse=True)
# print(a,b)
# ######3#######sorted的用法
# a=[1,2,3,6,9]
# a1=[2,24,3,6,9]
# b=sorted(a,reverse=True)
# print(a,b)

##test2
#lambda函数和reduce函数的使用
# from functools import reduce
# def add(x,y) :            # 两数相加
#     return   x+y
# sum1 = reduce(add, [3])   # 计算列表和：1+2+3+4+5
# sum2 = reduce(lambda x, y: x+y, "hey!","hello!world!")  # 使用 lambda 匿名函数
# sum3=add(7,1)
# print(sum1)
# print(sum2)
# print(sum3)

##test3
# a=2
# b=a
# c=b
# print(a,b,c)
# a=cmp(1,2)
# print(a,b,c)

##test4
# 获取列表的第二个元素
# def takeSecond(elem):
#     return elem[-1]
# # 列表
# random = [(2, 2,4), (3, 4,3), (4, 1,9), (1, 3,6)]
# # 指定第二个元素排序
# random.sort(key=takeSecond,reverse=True)
# # 输出类别
# print('排序列表：', random)

#test5
# a=int(input(":"))
# while a>5:
#     print("ok")
#     break
# else:
#     print("no")
#     input("again:")
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]]
# print(names)
#
# def Salary(x):
#     L_Salary =[]
#     for i in x:
#         L_Salary.append(i[5])
#     return L_Salary
# a=Salary(names)
# # B=[]
# # B.append('U')
# print(a)





# test6
#类的定义和使用
# class Fruit:
#     def grow(self):
#        print (self,"Fruit tree grow,",end='')
#     def deadhead(x,y,z):
#         print(x,"Fruit tree deadhead,",y,"bird flied,",z,"people gone.")
# Fruit.grow(3)
# Fruit.deadhead(4,3,9)

#test7
#python比较函数 cmp_to_key
from functools import cmp_to_key
# def tuple(x):
#     return x[2]
# x=10
# y=12
# mylist=[(2,3,4),(2,3,5),(11,2,7)]
# # a=cmp(x,y)
# b=sorted(mylist,key=tuple,reverse=True)
# print("     ",b)
# c=sorted(mylist)
# print(c)
# print(sorted("sorted(c)"))


# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]]
# class Company(object):
#     def __init__(self):
#         print("hello")
#     def Salary(x):
#         return x
#     def Sex(self):
#         return print("hello,man")
#     def Age(self):
#         return self
#     def __del__(self):
#         print("oh,god!")
#         return self
# # Ave_Salary=sum(Company.Salary(names))
# # print(Ave_Salary)
# Company.Salary(3)
# Company.Sex(2)
#
# def Department(self):
#     return print("success")
# Company.__init__(Department)
# del Company
# # print(Company)
#######
# class Employee:
#     def __init__(self):
#         print('Employee created')
# # Calling destructor
#     def __del__(self):
#         print("Destructor called")
#     def Create_obj():
#         print('Making Object...')
# obj = Employee()
# print('function end...')
# Employee.__init__()


# class Myclass:
#     i = 123
#
#     def __init__(self,friend):
#         self.friend = friend
#     def func(self,myself): #带有参数的类方法
#         self.myself = myself
#         return self.myself , "say hello to" ,self.friend
#
# use_class = Myclass("xiao")
# print("调用类的属性：",use_class.i)
# print("调用类的方法:", use_class)
# print("调用类的方法:", use_class.func("xiaoming"))
# print("调用类的方法:", use_class.func("xiaohong"))

#带参数构造
# class Foobar():
#     def __init__(self,x):
#         self.tim=x
# t1=Foobar(10)
# print(t1.tim)
# class Foobar():
#     def __init__(self,x):
#         self.tim= x*x
#         self.ok=x+x
# t1=Foobar(10)  #当函数
# print(t1.tim)
# print(t1.ok)

# a=[1,2,3,5]
# b=[2.3,3,5,6]
# print(a+b)

# a=56+19+19+45+45
# b=a/5
# print(a,b)

# def Sex(x):  ver1
#     L_sex=[]
#     for i in x:
#         L_sex.append(i[2])
#     return L_sex
# def Age(x):
#     L_age=[]
#     for i in x:
#         L_age.append(int(i[1]))
#     return L_age
# def Department(x):
#     L_department = []
#     for i in x:
#         L_department.append(i[6])
#     return L_department
# def Company(x):
#     L_company = []
#     for i in x:
#         L_company.append(i[4])
#     return L_company
# def Name(x):
#     L_name=[]
#     for i in x:
#         L_name.append(i[1])
#     return L_name
# def Worknumber(x):
#     L_worknumber=[]
#     for i in x:
#         L_worknumber.append(i[3])
#     return L_worknumber

a=[1,2,3,4]
str_a=[]
for i in a :
    str_a.append(str(i))
print(str_a)

