import random
import re
import time
import funcdb
import pymysql

# 首页面显示
info = '''
*{0}*
*{1}*
*{0}*
*{2}*
*{3}*
*{4}*
*{5}*
*{6}*
*{7}*
*{8}*
*{0}*
'''
print(info.format('*' * 34, '中国农业银行账户管理系统'.center(24, ' '), '选项'.center(32, ' '),
                  '1.开户'.center(32, ' '), '2.存款'.center(32, ' '), '3.取款'.center(32, ' '),
                  '4.转账'.center(32, ' '), '5.查询'.center(32, ' '), '6.退出'.center(32, ' ')))


# 定义添加用户信息的函数、账户密码检查的函数、余额变动的函数
def add_user():
    bank_Agr = {}
    print('正在创建账户……')
    for i in range(10):
        if i < 9:
            print('*', end='')
            time.sleep(0.3)
        else:
            print('*')
    # 查询数据库账号余量
    sql_accout_num = 'select count(*) from users'
    num = funcdb.select(sql_accout_num)
    if num[0][0] <= 100:
        while True:
            tem_account = []
            for i in range(6):
                tem_account.append(str(random.choice(range(10))))
            account = ''.join(tem_account)
            if account not in bank_Agr:  # 账户没有重复
                print('您的账号为%s\n请牢记您的账号！' % account)
                break
            else:
                continue
        while True:
            sort = input('请选择账户类型：')
            if sort == '1':
                sort = 'Ⅰ'
                break
            elif sort == '2':
                sort = 'Ⅱ'
                break
            elif sort == '0':
                return 1  # 中途退出，未成功创建账户
            else:
                print('暂未开通此类卡\n请输入1或2')
        while True:
            name = input('请输入姓名：')
            if name == '0':
                return 1  # 中途退出，未成功创建账户
            elif len(name) != 0 and name != '0':
                break
            else:
                print('此为必填项')
                continue
        while True:
            password = input('请输入密码：')
            if password == '0':
                return 1
            if password.isdigit() and len(password) == 6:
                break
            else:
                print('请输入6位数字')
                continue
        country = input('请填写地址\n国籍:')
        if country == '0':
            return 1
        else:
            pass
        province = input('省份：')
        if province == '0':
            return 1
        else:
            pass
        street = input('街道：')
        if street == '0':
            return 1
        else:
            pass
        tablet = input('门牌号：')
        if tablet == '0':
            return 1
        else:
            pass
        while True:
            check = input('请确认信息\n输入1或回车确定添加\n输入0退出添加')
            if check == 0:
                return 1
            elif check == '1' or check == '':
                break
            else:
                print('指令非法！')

        # 输入完成，将数据插入到数据库
        sql1 = 'insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())'
        param1 = [account, sort, 0, name, password, 0.00, '中国工商银行', country, province, street, tablet]
        funcdb.update(sql1, param1)
        sql11 = 'select registerdate from users where account= %s'
        param11 = [account, ]
        rg_time = funcdb.select(sql11, param11)
        info = '''
{}
账号：{}
类型：{}类账户
户名：{}
密码：******
余额：{}
状态：{}
开户行：{}
注册时间：{}
地址：
    国家：{}
    省份：{}
    街道：{}
    门牌号：{}
{}
        '''
        print(info.format('*' * 40, account, sort, name, 0, '正常', '中国工商银行', rg_time[0][0], country, province, street,
                          tablet, '*' * 40))
        return 2
    else:
        return 2


def check_account(account, password):
    sql1 = 'select count(*) from users where account=%s'
    param1 = [account, ]
    count = funcdb.select(sql1, param1)
    if count[0][0] == 1:
        sql2 = 'select password,`status` from users where account=%s'
        param2 = [account, ]
        tem_list = funcdb.select(sql2, param2)
        if password == tem_list[0][0] and tem_list[0][1] != '冻结':
            sql3 = 'update users set `status`= 0 where account=%s '
            param3 = [account, ]
            funcdb.update(sql3, param3)  # 刷新账号状态
            return 1  # 账号密码均正确，刷新账号状态
        else:
            if tem_list[0][1] != '冻结' and int(tem_list[0][1]) <= 2:
                sql31 = 'update users set `status`= `status`+1 where account=%s '
                param31 = [account, ]
                funcdb.update(sql31, param31)  # 增加错误次数
                if tem_list[0][1] == 3:
                    sql32 = 'update users set `status` = `冻结` where account=%s '
                    param32 = [account, ]
                    funcdb.update(sql32, param32)  # 冻结账号
                    return 2  # 账号正确密码错误次数超过限制，冻结账号
                else:
                    return 3  # 账号正确密码错误，更新账号错误次数，返回重新输入
            else:
                return 2  # 代表账号密码错误3次以上，账号冻结
    else:
        return 4  # 账号错误，返回重新输入


def balance_change(account, passowrd, money, way):  # 参数有账号、密码、金额、变动方式（存或取）
    if way == 1:
        sql4 = 'update users set money = money+%s where account=%s '
        param4 = [money, account]
        funcdb.update(sql4, param4)  # 余额变动
        return 1  # 操作成功
    else:
        sql41 = 'select money from users where account=%s'
        param41 = [account, ]
        tem_money = funcdb.select(sql41, param41)
        balance = float(tem_money[0][0])
        if money <= float(balance):
            sql42 = 'update users set money = money-%s where account=%s '
            param42 = [money, account]
            funcdb.update(sql42, param42)  # 余额变动
            return 1
        else:
            return 2  # 余额不足，操作失败


while True:  # 主程序循环
    index = input('请输入指令：')
    if index == '1':  # 开户
        ret = add_user()
        if ret == 1:
            print('已退出出开户模块')
        elif ret == 2:
            print('欢迎使用农业银行账户！')
        else:
            print('用户库已满，暂不支持开户！')
    elif index == '2':  # 存钱
        while True:
            account = input('请存款输入账号:')
            sql5 = 'select count(*) from users where account=%s'
            param5 = [account, ]
            count = funcdb.select(sql5, param5)
            if count[0][0] == 1:
                sql51 = 'select account,`name` from users where account=%s'
                param51 = [account, ]
                tem_list = funcdb.select(sql51, param51)
                print('账号:%s\n户民:%s' % (tem_list[0][0], tem_list[0][1]))
                while True:
                    check = input('请确认信息\n输入1或回车确定存款\n输入0退出存款:')
                    if check == '0':
                        break
                    elif check == '1' or check == '':
                        sql52 = 'select password from users where account=%s'
                        param52 = [account, ]
                        tem_password = funcdb.select(sql52, param52)
                        password = tem_password[0][0]
                        while True:
                            money = input('请输入金额:')
                            if money != '0' and (
                                    money.isdigit() or (money.count('.') == 1 and money.replace('.', '1').isdigit())):
                                money = float(money)
                                balance_change(account, password, money, 1)
                                sql52 = 'select money from users where account=%s'
                                param52 = [account, ]
                                tem_balance = funcdb.select(sql52, param52)
                                balance = tem_balance[0][0]
                                print('操作成功，当前余额为：%.2f\n请继续操作' % balance)
                            elif money == '0':
                                print('操作结束')
                                break
                            else:
                                print('输入非法')
                        break
                    else:
                        print('无效操作')
                break
            elif account == '0':
                print('操作结束')
                break
            else:
                print('账号不存在，请核对后重输')
    elif index == '3':
        while True:
            account = input('请输入取款账号：')
            if account == '0':
                break
            password = input('请输入取款账号密码：')
            if password == '0':
                break
            else:
                pass
            ret = check_account(account, password)
            if ret == 1:
                while True:
                    money = input('请输入取款金额:')
                    if money != '0' and (
                            money.isdigit() or (money.count('.') == 1 and money.replace('.', '1').isdigit())):
                        money = float(money)
                        ret = balance_change(account, password, money, -1)
                        if ret == 'b_c1':
                            sql6 = 'select money from users where account=%s'
                            param6 = [account, ]
                            tem_balance = funcdb.select(sql6, param6)
                            balance = tem_balance[0][0]
                            print('操作成功，当前余额为：%.2f\n请继续操作' % balance)
                        elif ret == 'b_c2':
                            sql61 = 'select money from users where account=%s'
                            param61 = [account, ]
                            tem_balance = funcdb.select(sql61, param61)
                            balance = tem_balance[0][0]
                            print('当前余额为：%.2f\n余额不足，操作失败' % balance)
                    elif money == '0':
                        print('操作结束')
                        break
                    else:
                        print('输入非法')
            elif ret == 2:
                print('账号错误次数超过限制，请到柜台解冻')
                continue
            elif ret == 3:
                sql62 = 'select sort from users where account=%s'
                param62 = [account, ]
                tem_sort = funcdb.select(sql62, param62)
                sort = tem_sort[0][0]
                print('账号密码错误%d次，超过3次将冻结' % sort)
            elif ret == 4:
                print('账号输入有误,请重新输入')
            else:
                pass
    elif index == '4':
        while True:
            out_account = input('请输入转账账号：')
            if out_account == '0':
                break
            out_password = input('请输入转账账号密码：')
            if out_password == '0':
                break
            ret = check_account(out_account, out_password)
            if ret == 1:
                while True:
                    in_account = input('请输入收款账号:')
                    sql71 = 'select count(*) from users where account=%s'
                    param71 = [in_account, ]
                    in_count = funcdb.select(sql71, param71)
                    if in_count[0][0] == 1:
                        sql72 = 'select account,name from users where account=%s'
                        param72 = [in_account, ]
                        tem_list = funcdb.select(sql72, param72)
                        print('账号:%s\n户民:%s' % (tem_list[0][0], tem_list[0][1]))
                        while True:
                            check = input('请确认信息\n输入1或回车确定转账\n输入0退出转账')
                            if check == '0':
                                break
                            elif check == '1' or check == '':
                                while True:
                                    money = input('请输入金额:')
                                    sql73 = 'select password from users where account=%s'
                                    param73 = [in_account, ]
                                    tem_password = funcdb.select(sql73, param73)
                                    in_password = tem_password[0][0]
                                    if money != '0' and (money.isdigit() or (
                                            money.count('.') == 1 and money.replace('.', '1').isdigit())):
                                        money = float(money)
                                        sql74 = 'select sort from users where account=%s'
                                        param74 = [in_account, ]
                                        tem_sort = funcdb.select(sql74, param74)
                                        sort = tem_sort[0][0]
                                        if sort == 'Ⅰ':
                                            if money <= 50000:
                                                ret = balance_change(out_account, out_password, money, -1)
                                                if ret == 1:
                                                    balance_change(in_account, in_password, money, 1)
                                                    sql61 = 'select money from users where account=%s'
                                                    param61 = [out_account, ]
                                                    tem_balance = funcdb.select(sql61, param61)
                                                    balance = tem_balance[0][0]
                                                    print('转账成功，您当前余额为：%.2f\n请继续操作' % balance)
                                                else:
                                                    balance_change(in_account, in_password, money, 1)
                                                    sql61 = 'select money from users where account=%s'
                                                    param61 = [out_account, ]
                                                    tem_balance = funcdb.select(sql61, param61)
                                                    balance = tem_balance[0][0]
                                                    print('当前余额为：%.2f\n余额不足，操作失败' % balance)
                                                    break
                                            else:
                                                print('超过本类型账户单笔转账限制，请重新输入')
                                        else:
                                            if money <= 20000:
                                                ret = balance_change(out_account, out_password, money, -1)
                                                if ret == 'b_c1':
                                                    balance_change(in_account, in_password, money, 1)
                                                    print('转账成功，请继续操作')
                                                else:
                                                    sql61 = 'select money from users where account=%s'
                                                    param61 = [out_account, ]
                                                    tem_balance = funcdb.select(sql61, param61)
                                                    balance = tem_balance[0][0]
                                                    print('当前余额为：%.2f\n余额不足，操作失败' % balance)
                                                    break
                                            else:
                                                print('超过本类型账户单笔转账限制，请重新输入')
                                    elif money == '0':
                                        print('操作结束')
                                        break
                                    else:
                                        print('输入非法')
                                break
                            else:
                                print('无效操作')
                        break
                    elif in_account == '0':
                        print('操作结束')
                        break
                    else:
                        print('账号输入错误或非本行账号，请核对后重输')
            elif ret == 2:
                print('账号错误次数超过限制，请到柜台解冻')
                continue
            elif ret == 3:
                sql75 = 'select `status` from users where account=%s '
                param75 = [out_account, ]
                times = funcdb.select(sql75, param75)
                print('账号密码错误%s次，超过3次将冻结' % times[0][0])
            elif ret == 4:
                print('账号输入有误,请重新输入')
            else:
                pass
    elif index == '5':
        while True:
            account = input('请输入查询账号：')
            if account == '0':
                break
            else:
                pass
            password = input('请输入查询账号密码：')
            if password == '0':
                break
            else:
                pass
            ret = check_account(account, password)
            if ret == 1:
                sql_search = 'select * from users where account=%s'
                para_search = [account, ]
                tem_list_search = funcdb.select(sql_search, para_search)
                column_name = ['账号', '卡类', '状态', '户名', '密码', '余额', '开户行', '国家', '省份', '街道', '门牌号']
                dict_info = dict(zip(column_name, tem_list_search[0]))
                print('查询成功！\n', '*', '中 国 农 业 银 行'.center(33, ' '), '*')
                print('*' * 36)
                for key, value in dict_info.items():
                    if key == '状态':
                        if value != '冻结':
                            print(key, ':', '正常')
                        else:
                            print(key, ':', value)
                    else:
                        print(key, ':', value)
                print('*' * 36)
                break
            elif ret == 2:
                print('账号错误次数超过限制，请到柜台解冻')
                continue
            elif ret == 3:
                sql8 = 'select sort from users where account=%s'
                param8 = [account, ]
                times = funcdb.select(sql8, param8)
                print('账号密码错误%d次，超过3次将冻结' % times[0][0])
            elif ret == 4:
                print('账号输入有误,请重新输入')
            else:
                pass
    elif index == '6':
        print('Bye!')
        break
    else:
        print('无效指令')
        continue
