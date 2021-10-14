"""
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
任务：优惠券加上随机获得一张优惠券（9折10，5折3，免费的1：单个商品打折9折10，5折3，免费的1）
"""

import random

shop = [["戴尔", 19999], ["电磁炉", 199], ["A4纸", 9.9], ["华为P50 4G", 5000],['耳机',50],['抱枕',80],['洗衣粉',21],['电冰箱',800],['铅笔',2],['糖果',0.5]]
shop1 = dict(shop)
while True:  # 初始化余额
    money = input("请输入您的余额：")
    if money.isdigit() or money.count(".") == 1:
        money = float(money)
        money_origin = money
        break
    else:
        print("需要输入数字")
coupon = 1  # 生成优惠券  9折10，5折3，免费的1
randint = random.randint(1, 15)
if 1 <= randint <= 10:
    coupon = 0.9
    print("您获得一张单次9折券")
elif 10 < randint <= 13:
    coupon = 0.5
    print("您获得一张单次5折券")
else:
    coupon = 0
    print("恭喜您获得1张单次免费券")
mycart = {}  # 准备一个购物车
origin_coupon=coupon*10
save=0


def Purch(x, y, z, n):  # 定义一个购买的函数 #自动量分别商品编号，余额，折扣券 数量
    tem_list = {'Money': y, 'Coupon': z, 'num':n, 'discount':0}
    if shop[x][1] * z *n <= y:
        discount = 'n'
        tem_list = {'Money': y, 'Coupon': z, 'num':n, 'discount':0}
        if z != 1:
            if z == 0:
                discount = input('您有一张免费券，输入y使用，默认为不使用）：')
            elif z == 0.5:
                discount = input('您有一张五折券，输入y使用，默认为不使用：')
            else:
                discount = input('您有一张九折券，输入y使用，默认为不使用：')
        if discount == 'y':
            y = y - shop[x][1] * z*n
            n = mycart.get(shop[x][0],0)+n
            s = shop[x][1]* (1-z) * n
            z = 1
            print("购买", n,'件',shop[x][0],"成功")
            print('已购买：', mycart)
            print('您的当前余额为：', y)
            tem_list['Money'] = y
            tem_list['Coupon'] = z
            tem_list['num'] = n
            tem_list['discount'] = s
            return tem_list
        else:
            if shop[x][1]*n <= y:
                y = y - shop[x][1]*n
                n = mycart.get(shop[x][0],0) + n
                print("购买", n, '件', shop[x][0], "成功")
                print('已购买：', mycart)
                print('您的当前余额为：', y)
                tem_list['Money'] = y
                tem_list['Coupon'] = z
                tem_list['num'] = n
                return tem_list
            else:
                print('您的余额不足，当前余额为：', y)
                return tem_list
    else:
        print('您的余额不足，当前余额为：', y)
        return tem_list


while True:
    for index, value in enumerate(shop):  # 展示商品
        print(index, ":", value)
    chose = input("请输入商品编号：")  # 输入的还是str
    if chose.isdigit():  # 判断是否是数字
        chose = int(chose)
        if chose > len(shop) - 1:
            print("这里没有您需要的商品")
        else:
            while True:
                num = input('请输入购买数量：')
                if num.isdigit():
                    num=int(num)
                    list = Purch(chose, money, coupon, num)  # 进行购买
                    money = list['Money']
                    coupon = list['Coupon']
                    num = list['num']
                    mycart[shop[chose][0]]=mycart.get(shop[chose][0],0)+num
                    save += list['discount']
                    break
                elif num == 'q' or num == '0':
                    break
                else:print("输入非法！")
    elif chose == "q" or chose == "Q":
        #    打印购物小条
        a = '谢谢惠顾'
        print(a.center(20, '#'))
        print('-' * 20)
        if len(mycart) != 0:
            print('您购买了：\n')
            # mycart_final = {}
            # for i in mycart:
            #     if i not in mycart_final:
            #         mycart_final[i] = 1
            #     else:
            #         mycart_final[i] += 1
            # print(mycart_final)
            print("%-13s%-13s%-13s%-13s" % ("商品", '数量', '单价', '总价'))
            for key, value in dict.items(mycart):
                print('%-13s%-13d%-13.2f%-13.2f' % (key, value, shop1[key],shop1[key]*mycart[key]))
            print('%-13s%-13s%-13s%-13.2f ' % ('总消费', '-', '-', money_origin - money))
            if coupon == 1:
                print("使用了一张%d折优惠券" % origin_coupon)
                print('节省了%.2f' % float(save))
        else:
            print('您未购买任何商品')
            print(mycart)
        print("当前余额：%-10.2f" % money)
        break
    else:  # 不是数字
        print("输入错误")
