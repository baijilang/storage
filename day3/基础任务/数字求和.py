'''
10个数字求和
#优化：1.输入任意数量的数字，进行计算，输入非数字形式的字符出现提示
       2.支持小数，负数
       3.q退出
       4.输入最大值、和、平均值
'''
###################################################
while True:
    list1=input("输入数字,使用英文逗号隔开：")
    list=list1.split(",")
    sum_list=0
    max_list=list[0]
    if list[-1]!="" and list[-1]!="q":
        for i in range(0,len(list)):
            if (list[i].startswith("-") and list[i].count("-")==1) or (list[i].count("-")==0):
                if list[i].count(".")<=1:
                    if ((list[i].replace(".","1")).replace("-","1")).isdigit():
                        sum_list=sum_list + float(list[i])
                        if float(list[i])>=float(max_list):
                            max_list=float(list[i])
                        if i==len(list)-1:
                            print("MAX=%d" % (max_list))
                            print("SUM=%.2f" % (sum_list))
                            print("AVE=%.2f" % (sum_list / len(list)))
    elif list[-1]=="":
        print("最后一个字符不能为空")
    elif list[-1]=="q":
        break
    else:
         continue

