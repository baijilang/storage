"""dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key
#2、请循环遍历出所有的value
# 3、请在字典中增加一个键值对,"k4":"v4"  """

# 1.遍历字典
print('1.遍历字典')
dict1 = {"k1": "v1", "k2": "v2", "k3": "v3"}
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)
print('===============================================')



# 小明去超市购买水果，账单如下
# 苹果  32.8
# 香蕉  22
# 葡萄  15.5
# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
# 用水果名称做key，金额做value，创建一个字典
# info = {
#     '苹果':32.8,
#     '香蕉': 22,
#     '葡萄': 15.5}

# 2.字典创建，查询
print('2.字典创建，查询')
fruits = ['苹果', '香蕉', '葡萄']
prices = [32.8, 22, 15, 5]
info = dict(zip(fruits,prices))
print(info)
print(info['苹果'])
print('===============================================')


# 小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
# 以姓名做key，value仍然是字典
# }
# 3.字典查找，计算
print('3.字典查找，计算')
fruit_price= {'苹果':12.3,
            '草莓':4.5,
             '香蕉':6.3,
             '葡萄':5.8,
            '橘子':6.4,
            '樱桃':15.8}
info = {
    '小明': {
    'fruits': {'苹果':4, '草莓':13, '香蕉':10},
    'money':None},
'小刚': {
    'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
    'money': None}
}


def single_money(x,y):
    money1 = info[x]['fruits'][y] * fruit_price[y]
    return money1


info['小明']['money'] = single_money('小明','苹果') + single_money('小明','草莓') + single_money('小明','香蕉')
info['小刚']['money'] = single_money('小刚','葡萄') + single_money('小刚','橘子') + single_money('小刚','樱桃')
print(info)
print('小明花费%.2f 小刚花费%.2f' % (info['小明']['money'], info['小刚']['money']))
print('===============================================')


# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
# 4.字典计数
print('4.字典计数')
list1 = [21]*3
list2 = [56]*9
list3 = [10]*3
dict_all = list1 + list2 + list3
dict_count = {}
for i in dict_all:
    if i not in dict_count:
        dict_count[i] = 1
    else:
        dict_count[i] += 1
print(dict_count)
print('===============================================')


# 有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# # 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# 5.录入字典值
print('5.录入字典值')
list = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
name=[]
message=[]
for i in range(len(list)):
    name.append(list[i][0])
    message.append(list[i][1:7])
info=dict(zip(name,message))
print(info)
# ===============================================

