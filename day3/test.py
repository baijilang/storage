
# import random
# list=["陆梓言","郭洪波","方则属","签","千纸鹤","EXO"]
# print("============欢迎来到处罚系统===============")
# while 1==1:
#     inex=input("输入1开始选人")
#     ran=random.randint(0,len(list)-1)#len==6  范围是0-6全部可以取到
#     inex1=input("输入2开始生成处罚编数")
#     num=random.randint(0,90)
#     print(list[ran],"处罚了",num,"遍")
# # a=[12,2]
# names=a
# print(names)

'''
添加 list.append  .extend  .insert(A,B)
删除 list.remove() 删除list里面特定的元素
    del list[n] 删除list的角标为n的元素
    N=m.pop 将列表最后一个元素返回赋值给N,并删除列表中的该元素
列表分片 N=list[A:B] N得到list中角标为A到B的元素

'''
# c=['a','b']
# ch=3
# d=[1,2]
# e=[]
# for w  in c : print(c)
# for q  in d : print(d)
# print(e)
# e.append(d)
# print(e)
# list=[1,2,3,10]
# list[0]=5
# print(list[-1])
def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()