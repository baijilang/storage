all_month_data = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None,
                  9: None, 10: None, 11: None, 12: None}
clothes_data = {'羽绒服': [0, 0, 0]}  # 关键字是种类，值里面：[0]价格  [1]是数量  [2]是总价
clothes_all_data = {'羽绒服': [0, 0, 0]}  # 多个月的衣服数据
clothes_name_list = []
list1 = {}  # 衣服的数量价格
list2 = []
price_sum = 0
count_sum = 0
l_cloth = []


# 获取某月的所有数据
def month_data(month):
    import xlrd
    wb = xlrd.open_workbook(filename=r'2020年每个月的销售情况.xlsx', encoding_override=True)
    all_month_data[month] = wb.sheet_by_index(int(month) - 1)
    return 1


# 获取某月所有衣服的种类
def clothes_name(month):
    global clothes_name_list
    clothes_name_list = []  # 清空原内容
    month_data(month)
    row = all_month_data[month].nrows
    for i in range(1, row):
        if all_month_data[month].row_values(i)[1] not in clothes_name_list:  # 没有出现的名字
            clothes_name_list.append(all_month_data[month].row_values(i)[1])  # 将名字添加到表里面


# 获取某月 、某种衣服的价格、数量、总价、
def cloth_month(cloth_name, month):
    month_data(month)
    row = all_month_data[month].nrows
    clothes_data[cloth_name] = [0, 0, 0]  # 清空上次计算的数量
    for i in range(1, row):
        if all_month_data[month].row_values(i)[1] == cloth_name:
            clothes_data[cloth_name][0] = all_month_data[month].row_values(i)[2]
            clothes_data[cloth_name][1] += all_month_data[month].row_values(i)[4]
            clothes_data[cloth_name][2] += clothes_data[cloth_name][0] * all_month_data[month].row_values(i)[4]
    return 1  # 当月价格、数量、总价统计成功


# 某几个月，某几种衣服的销售总额\数量，参数为列表或序列
def all_months(l_clo, l_mon):
    global price_sum, count_sum, clothes_data, list1
    list1 = {}
    clothes_data = {}
    for i in l_clo:
        price_sum = 0
        count_sum = 0
        for j in l_mon:
            cloth_month(i, j)
            count_sum += clothes_data[i][1]
            price_sum += clothes_data[i][2]
        list1[i] = [clothes_data[i][0], count_sum, price_sum]
    return 1


# 某些月份中出现过的衣服列表
def l_clo(monthlist):
    global l_cloth
    l_cloth = []
    for i in monthlist:
        clothes_name(i)
        for j in clothes_name_list:
            if j not in l_cloth:
                l_cloth.append(j)
    return 1


# 全年衣服销售量排名函数
def rank(way, dic):
    num = dic[1]['羽绒服'][0]
    if way == 1:
        for i in dic.values():
            for j in i.values():
                if j[0] > num:
                    num = j[0]
        for i in dic.values():
            for key, value in i.items():
                if value[0] == num:
                    print('销售最多衣服是%s' % key)
    else:
        for i in dic.values():
            for j in i.values():
                if j[0] < num:
                    num = j[0]
        for i in dic.values():
            for key, value in i.items():
                if value[0] == num:
                    return [key, value[0]]


# 销售总额、销售量合计
def all_sals(monthlist):
    annual_sals = 0
    annual_count = 0
    l_clo(monthlist)
    lclo = l_cloth
    all_months(lclo, monthlist)
    a = list1
    for i in a.values():
        annual_sals += i[2]
        annual_count += i[1]
    return [annual_count, annual_sals]


# 每件衣服年销售占比，销售最多和最低的
def per_clo(monthlist):
    all = all_sals(monthlist)
    l_clo(monthlist)
    all_months(l_cloth, monthlist)
    global list2
    list2 = []
    for key, value in list1.items():
        print('__{}__销售量：{:.0f}件,占比{:.2%}；销售额：{:.2f}，占比{:.2%}'.format(key, value[1], value[1] / all[0], value[2],
                                                                      value[2] / all[1]))
        list2.append([key, value[1], value[1] / all[0], value[2], value[2] / all[1]])
    return 1


# 1、年销售总额

'''print('年销售总额为：%.2f' % all_sals(range(1,13))[1])'''

# 2、年销售占比、畅销衣物
'''print('年销售占比————————')
per_clo(range(1, 13))
l_max = sorted(list2, key=lambda x: x[1], reverse=True)
print('最畅销的是：', l_max[0][0], '\t\t', '销售最低的是:', l_max[-1][0])'''

# 3、季度销售占比、畅销衣物
'''# s1
print('第一季度销售占比————————')
per_clo((2,3,4))
l_max = sorted(list2, key=lambda x: x[1], reverse=True)
print('最畅销的是：', l_max[0][0], '\t\t', '销售最低的是:', l_max[-1][0])

# s2
print('第二季度销售占比————————')
per_clo((5,6,7))
l_max = sorted(list2, key=lambda x: x[1], reverse=True)
print('最畅销的是：', l_max[0][0], '\t\t', '销售最低的是:', l_max[-1][0])

# s3
print('第三季度销售占比————————')
per_clo((8,9,10))
l_max = sorted(list2, key=lambda x: x[1], reverse=True)
print('最畅销的是：', l_max[0][0], '\t\t', '销售最低的是:', l_max[-1][0])

# s4
print('第四季度销售占比————————')
per_clo((11,12,1))
l_max = sorted(list2, key=lambda x: x[1], reverse=True)
print('最畅销的是：', l_max[0][0], '\t\t', '销售最低的是:', l_max[-1][0])'''