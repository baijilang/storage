'''
需求：
    input：
    1.输入参与人数
    2.输入排除人数
    3.输入输入步长
    output：
    1.排列顺序
'''
print("==========基督徒问题==========\n#1代表基督徒，0代表非基督徒")

amount_a=1
step=1
amount_A=input("输入总人数：")
while True:
    if amount_A.isdigit() and int(amount_A)!=0:
        break
    elif amount_A=="q":
        break
    elif amount_A=="":
        amount_A=input("重新输入总人数：")
    else:
        amount_A=input("重新输入总人数：")
if amount_A!="q":
    amount_a = input("输入非基督徒人数：")
    while True:
        if amount_a.isdigit() and (int(amount_a)<=int(amount_A)):
            break
        elif amount_a=="q":
            break
        elif (amount_a.isdigit()) and (int(amount_a)>int(amount_A)):
            amount_a=input("非基督徒人数过大请重输：")
        elif amount_a=="" :
            amount_a=input("重新输入非基督徒人数：")
        else :
            amount_a=input("重新输入非基督徒人数：")
if amount_A!="q" and amount_a!="q":
    step = input("输入步长：")
    while True:
        if step.isdigit() and int(step)!=0:
            break
        elif step =="q":
            break
        else:
            step=input("重新输入步长：")   #输入q退出代码的执行，只有所有地方放输入正确才可进行下一步
if amount_A.isdigit() and amount_a.isdigit() and step.isdigit():
    m=int(amount_A)
    n=int(amount_a)
    q=int(step)
    list=[]
    for i in range(m):
        list.append(1)
    #数值合理的话，进行接下来的运算
    k=0
    v_step = q
    t_step = q
    while True:
        if k<n :  #标记的人数是否到达要求，没有的话进入循环
            if v_step <= m:  #还没有转过一圈时
                if t_step%q==0:  #这一步是不是到排除人了
                    list[v_step-1]=0
                    v_step+=1
                    t_step+=1
                    k+=1
                else :
                    v_step += 1
                    t_step += 1
            else :  #计数超过一圈的时候
                if list[v_step%m-1]==1:   #超过一圈时判断当下的位置，如果有人
                    if t_step%q==0:         #看是否到排除人的时候
                        list[v_step%m-1]=0
                        v_step += 1
                        t_step += 1
                        k+=1                  #排除人记得记录到排除人数
                    else:                    #没到的话向前走一步
                        v_step += 1
                        t_step += 1
                else:                       #当下没有人，向后看一步
                    v_step += 1
        else:
            print(list)
            break









