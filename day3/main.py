'''
有一个列表里面有人名
随机生成选择一人
随机生成处罚遍数

优化代码：一个输入进行判断，可预先输入参与者，以及惩罚上限，输入数字可以从以上随机选人受罚，支持中途退出
'''
import random
print("========惩罚游戏========\ntips1.输入任何纯数字开始选人，并随机生成处罚遍数\ntips2.输入q或回车退出游戏")
names=[]  #定义一个数组，接收输入的参与人
global name
name=1
TIME=input("请输入最大惩罚次数:")
while True:
    if TIME.isdigit() and (name!="q" or name!=""):
        while True:
            name=input("请输入代号：")
            if name == "q" or name=="" :
                break
            elif name.isdigit():
                if len(names)!=0:
                    ran_index=random.randint(0,len(names)-1)
                    ran_times=random.randint(0,int(TIME))
                    print("%s接受惩罚%d次"%(names[ran_index],ran_times))
                else:
                    print("没有参与者")
            elif name=="list":
                print(names)
            else:
                names.append(name)
                continue
        break
    elif (TIME=="q" or TIME=="") or (name=="q" or name==""):
        break
    else :
        TIME=input("请重输惩罚次数：")


