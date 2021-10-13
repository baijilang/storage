#有下列人员数据库，请按要求实现
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
'''names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]'''
#1.计算平均薪资
#2.计算平均年龄
#3.将公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
#4.计算男女人数，比例
#7.统计每个部门的人数
#########################################
print("=================人员数据库查询=================")
print("常用指令——平均薪水：1  平均年龄：2  男女比例：3  查询项目：4\n添加人员：5  查看总表：6  统计：7")
print("项目代号——姓名:1 年龄:2 性别:3 编号:4 公司:5 薪水:6 部门编号:7；")
print("字段代号——全部：all  \n输入其他字符进行该字段的查找")
print("退出及返回上一步：q")
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]]
def number_Ave(x,y):
    number_list=[]
    for i in x:
        n=i[y]
        number_list.append(n)
        x=number_list
    sum=0
    for i in x:
        sum+=float(i)
    Ave=sum/len(x)
    return Ave
def str_count(x,y,z):
    list=[]
    for i in x:
        n=i[y]
        list.append(n)
    count=0
    for i in list:
        if i==z:
            count+=1
    return count
def str_look(x,y):
    list=[]
    for i in x:
        n=i[y]
        list.append(n)
    return list
Ave_salary=number_Ave(names,5)  #平均工资
Ave_age=number_Ave(names,1)
Bal_sex1=str_count(names,2,"男")/len(names)
Bal_sex0=str_count(names,2,"女")/len(names)
Apa_count60=str_count(names,6,"60")
while True:
    order=input("请输入常用指令：")
    if order=="1":
        print("平均薪水：%.2f元"%(Ave_salary))
    elif order=="2":
        print("平均年龄：%.2f岁"%(Ave_age))
    # elif order=="3":
    elif order=="3":
        sex1=str_count(names, 2, "男")
        sex0=str_count(names, 2, "女")
        Bal_sex1 = str_count(names, 2, "男") / len(names)
        sext1=format(Bal_sex1,'.2%')
        Bal_sex0 = str_count(names, 2, "女") / len(names)
        sext0=format(Bal_sex0,'.2%')
        print("男性%d人，占%s\n女性%d人，占%s"%(sex1,sext1,sex0,sext0))
    elif order=="4":
        while True:
            a=input("输入查询的项目(1-7)：")
            if a.isdigit() and int(a)>=1 and int(a)<=7:
                while True:
                    b=input("输入查询字段：")
                    all = str_look(names,int(a)-1,)
                    if b=="all":
                        print(all)
                    else:
                        if b=="q":
                            break
                        else:
                            c=str_count(names,int(a)-1,b)
                            print("查询到“%s”的数量为：%d"%(b,c))
            elif a=="q":
                break
    elif order =="5" :
        while True:
            tem_list=[]
            name=input("姓名：")
            if name=="q":
                break
            else:tem_list.append(name)
            while True:
                age=input("年龄：")
                if age.isdigit:
                    break
                elif age=="q":
                    break
                else:
                    continue
            if age=="q":
                break
            else:tem_list.append(age)
            while True:
                sex=input("性别：")
                if sex=="男" or sex=="女":
                    break
                elif sex=="1" :
                    sex="男"
                    break
                elif sex=="0":
                    sex="女"
                    break
                elif sex=="q":
                    break
                else:print("输入非法请重输入")
            if sex=="q":
                break
            else:tem_list.append(sex)
            while True:
                wnum=input("编号：")
                if wnum.isdigit:
                    break
                elif wnum=="q":
                    break
                else:print("输入非法请重输入")
            if wnum=="q":
                break
            else:tem_list.append(wnum)
            company=input("公司：")
            if company=="q":
                break
            else:tem_list.append(company)
            while True:
                salary=input("薪水：")
                if salary.isdigit  or (salary.replace(".",1).isdigit()):
                    break
                elif salary=="q":
                    break
                else:print("输入非法请重输入")
            if salary=="q":
                break
            else:tem_list.append(salary)
            while True:
                apartment=input("部门编号:")
                if apartment.isdigit:
                    break
                elif apartment=="q":
                    break
                else:print("输入非法请重输入")
            if apartment=="q":
                break
            else:tem_list.append(apartment)
            names.append(tem_list)
            Ave_salary =number_Ave(names,5) # 平均工资
            Ave_age = number_Ave(names,1) # 平均年龄
            print("添加成功")
    elif order=="6":
        print("【 姓名   年龄   性别   编号   公司   薪水   部门编号】")
        for i in names:print(i)
    elif order=="7":
        while True:
            a=input("输入统计的项目(1-7)：")
            if a.isdigit() and int(a)>=1 and int(a)<=7:
                while True:
                    b=input("输入统计字段：")
                    all_list = str_look(names,int(a)-1,)
                    if b=="all":
                        print(all_list)
                        percent_all=[]
                        list_name=[]
                        list_per=[]
                        for i in range(len(all_list)):
                            if i==0:
                                list_name.append(all_list[i])
                            else:
                                for m in range(i+1) :
                                    if all_list[m]!=all_list[i]:
                                        list_name.append(all_list[i])
                        for i in range(len(list_name)):
                            c=all_list.count(list_name[i])/len(all_list)
                            c=format(c,'.2%')
                            list_per.append(c)
                        percent_all=dict(zip(list_name,list_per))
                        print("所有字段比例如下：",'\n',percent_all)
                    else:
                        if b=="q":
                            break
                        elif b.isdigit() or b.count(".")==1:
                            c = format(str_count(names, int(a) - 1, float(b)) / len(all_list), '.2%')
                            print("查询到“%s”的占比为：%s" % (b, c))
                        else:
                            c=format(str_count(names,int(a)-1,b)/len(all_list),'.2%')
                            print("查询到“%s”的占比为：%s"%(b,c))
            elif a=="q":
                break
    elif order=="q":
        break
    else:print("无效指令")







