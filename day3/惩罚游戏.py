'''
有一个列表里面有人名
随机生成选择一人
随机生成处罚遍数

ver1.0优化代码：一个输入进行判断，可预先输入参与者，以及惩罚上限，输入数字可以从以上随机选人受罚，
支持查看参与者
支持中途退出
ver2.0
自动将重复的参与者剔除
增加消耗金币、金币充值功能
实时查看剩余金币和游玩次数
'''


###############################################################################
import random
print("===============惩罚游戏2.0===============\ntips1.代号输入任何纯数字开始选人，并随机生成处罚遍数")
print("tips2.代号输入F可以查看以玩次数和剩余金币\ntips3.输入list查看参与者\n代号输入q或回车退出游戏")
print("tips4.初始金币为100，每次使用消耗10金币，金币不足时再次使用会锁定")
names=[]  #定义一个数组，接收输入的参与人
# global name
name=1
TIME=input("请输入最大惩罚次数:")
coin=100
play_times=0
while True:
    if TIME.isdigit() and (name!="q" or name!="") :
        while True:
            name=input("请输入代号：")
            if name in names:print("已添加过参与者")
            elif coin<10:
                print("金币不足")
                recharge=input("请输入充值密码或其他任意字符退出：")
                if recharge=="qwerty":
                    coin=100
                    print("成功充值100金币")
                else:
                    break
            else:
                if name == "q" or name=="" :
                    break
                elif (name == "F"):
                    print("剩余金币：%d，已玩次数：%d" % (coin, play_times))
                elif name.isdigit():
                    if len(names)!=0:
                        ran_index=random.randint(0,len(names)-1)
                        ran_times=random.randint(0,int(TIME))
                        print("%s接受惩罚%d次"%(names[ran_index],ran_times))
                        coin-=10
                        play_times+=1
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


