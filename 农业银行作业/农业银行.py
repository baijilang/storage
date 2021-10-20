import random
import re
import time

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
*{9}*
*{0}*
'''
print(info.format('*' * 34, '中国农业银行账户管理系统'.center(24, ' '), '选项'.center(32, ' '),
                  '1.开户'.center(32, ' '), '2.存款'.center(32, ' '), '3.取款'.center(32, ' '),
                  '4.转账'.center(32, ' '), '5.查询'.center(32, ' '), '6.退出'.center(32, ' '), '0.后退'.center(32, ' ')))
bank_Agr = {}     # 定义一个字典存放账户信息
# 字典内容格式   bank={None: {'类型': None, '状态': 0, '户名': None, '密码': None, '余额': None, '开户行': '中国农业银行',
#                    '地址': {'国家': None, '省份': None, '街道': None, '门牌号': None}}}
# 定义添加用户信息的函数、账户密码检查的函数、余额变动的函数
def add_user():
    print('正在创建账户……')
    for i in range(10):
        if i < 9:
            print('*',end='')
            time.sleep(0.3)
        else:print('*')
    if len(bank_Agr) <= 100:
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
                return 'a1'  # 中途退出，未成功创建账户
            else:
                print('暂未开通此类卡\n请输入1或2')
        while True:
            name = input('请输入姓名：')
            if name == '0':
                return 'a1'  # 中途退出，未成功创建账户
            elif len(name) != 0 and name != '0':
                break
            else:
                print('此为必填项')
                continue
        while True:
            tem_password = input('请输入密码：')
            if tem_password == '0':
                return 'a1'
            p_password = r'^[0-9]{6}$'
            password = re.match(p_password, tem_password)
            if password == None:
                print('请输入6位数字')
            elif len(tem_password) == 6:
                password = password.group()
                break
            else:
                print('请输入6位数字')
                continue
        country = input('请填写地址\n国籍:')
        if country == '0':
            return 'a1'
        else:
            pass
        province = input('省份：')
        if province == '0':
            return 'a1'
        else:
            pass
        street = input('街道：')
        if street == '0':
            return 'a1'
        else:
            pass
        tablet = input('门牌号：')
        if tablet == '0':
            return 'a1'
        else:
            pass
        while True:
            check = input('请确认信息\n输入1或回车确定添加\n输入0退出添加')
            if check == 0:
                return 'a1'
            elif check == '1' or check == '':
                break
            else:
                print('指令非法！')
        bank_Agr[account] = {}
        bank_Agr[account]['户名'] = name
        bank_Agr[account]['类型'] = sort
        bank_Agr[account]['密码'] = password
        bank_Agr[account]['余额'] = 0.00
        bank_Agr[account]['状态'] = 0
        bank_Agr[account]['开户行'] = '中国农业银行'
        bank_Agr[account]['地址'] = {}
        bank_Agr[account]['地址']['国家'] = country
        bank_Agr[account]['地址']['省份'] = province
        bank_Agr[account]['地址']['街道'] = street
        bank_Agr[account]['地址']['门牌号'] = tablet
        info = '''
{}
账号：{}
类型：{}类账户
户名：{}
密码：******
余额：{}
状态：{}
开户行：{}
地址：
    国家：{}
    省份：{}
    街道：{}
    门牌号：{}
{}
        '''
        print(info.format('*' * 40, account, sort, name, 0, '正常', '中国农业银行', country, province, street, tablet, '*' * 40))
        return 'a2'
    else:
        return 'a3'
def check_account(account, password):
    if account in bank_Agr.keys():
        if password == bank_Agr[account]['密码'] and str(bank_Agr[account]['状态']) != '冻结':
            bank_Agr[account]['状态'] = 0
            return 'c_a1'  # 账号密码均正确，刷新账号状态
        else:
            if str(bank_Agr[account]['状态']) != '冻结':
                bank_Agr[account]['状态'] += 1
                if bank_Agr[account]['状态'] == 3:
                    bank_Agr[account]['状态'] = '冻结'
                    return 'c_a2'  # 账号正确密码错误次数超过限制，冻结账号
                else:
                    return 'c_a3'  # 账号正确密码错误，更新账号错误次数，返回重新输入
            else:
                return 'c_a2'  # 代表账号密码错误3次以上，账号冻结
    else:
        return 'c_a4'  # 账号错误，返回重新输入
def balance_change(account, passowrd, money, way):  # 参数有账号、密码、金额、变动方式（存或取）
    if way == 1:
        bank_Agr[account]['余额'] += money
        return 'b_c1'  # 操作成功
    else:
        if money <= bank_Agr[account]['余额']:
            bank_Agr[account]['余额'] -= money
            return 'b_c1'
        else:
            return 'b_c2'  # 余额不足，操作失败


while True:  # 主程序循环
    index = input('请输入指令：')
    if index == '1':  # 开户
        ret = add_user()
        if ret == 'a1':
            print('已退出出开户模块')
        elif ret == 'a2':
            print('欢迎使用农业银行账户！')
        else:
            print('用户库已满，暂不支持开户！')
    elif index == '2':  # 存钱
        while True:
            account = input('请存款输入账号:')
            if account in bank_Agr:
                print('账号:%s\n户民:%s' % (account, bank_Agr[account]['户名']))
                while True:
                    check = input('请确认信息\n输入1或回车确定存款\n输入0退出存款:')
                    if check == '0':
                        break
                    elif check == '1' or check == '':
                        password = bank_Agr[account]['密码']
                        while True:
                            money = input('请输入金额:')
                            if money != '0' and (
                                    money.isdigit() or (money.count('.') == 1 and money.replace('.', '1').isdigit())):
                                money = float(money)
                                balance_change(account, password, money, 1)
                                print('操作成功，当前余额为：%.2f\n请继续操作' % bank_Agr[account]['余额'])
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
            if ret == 'c_a1':
                while True:
                    money = input('请输入取款金额:')
                    if money != '0' and (money.isdigit() or (money.count('.') == 1 and money.replace('.', '1').isdigit())):
                        money = float(money)
                        ret = balance_change(account, password, money, -1)
                        if ret == 'b_c1':
                            print('操作成功，当前余额为：%.2f\n请继续操作' % bank_Agr[account]['余额'])
                        elif ret == 'b_c2':
                            print('当前余额为：%.2f\n余额不足，操作失败' % bank_Agr[account]['余额'])
                    elif money == '0':
                        print('操作结束')
                        break
                    else:
                        print('输入非法')
            elif ret == 'c_a2':
                print('账号错误次数超过限制，请到柜台解冻')
                continue
            elif ret == 'c_a3':
                print('账号密码错误%d次，超过3次将冻结' % bank_Agr[account]['状态'])
            elif ret == 'c_a4':
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
            if ret == 'c_a1':
                while True:
                    in_account = input('请输入收款账号:')
                    if in_account in bank_Agr:
                        print('账号:%s\n户民:%s' % (in_account, bank_Agr[in_account]['户名']))
                        while True:
                            check = input('请确认信息\n输入1或回车确定转账\n输入0退出转账')
                            if check == '0':
                                break
                            elif check == '1' or check == '':
                                while True:
                                    money = input('请输入金额:')
                                    in_password = bank_Agr[in_account]['密码']
                                    if money != '0' and (money.isdigit() or (
                                            money.count('.') == 1 and money.replace('.', '1').isdigit())):
                                        money = float(money)
                                        if bank_Agr[in_account]['类型'] == 'Ⅰ':
                                            if money <= 50000:
                                                ret = balance_change(out_account, out_password, money, -1)
                                                if ret == 'b_c1':
                                                    balance_change(in_account, in_password, money, 1)
                                                    print('转账成功，您当前余额为：%.2f\n请继续操作' % bank_Agr[out_account]['余额'])
                                                else:
                                                    print('当前余额为：%.2f\n余额不足，操作失败' % bank_Agr[out_account]['余额'])
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
                                                    print('当前余额为：%.2f\n余额不足，操作失败' % bank_Agr[out_account]['余额'])
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
            elif ret == 'c_a2':
                print('账号错误次数超过限制，请到柜台解冻')
                continue
            elif ret == 'c_a3':
                print('账号密码错误%d次，超过3次将冻结' % bank_Agr[out_account]['状态'])
            elif ret == 'c_a4':
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
            if ret == 'c_a1':
                print('查询成功！\n', '*', '中 国 农 业 银 行'.center(33, ' '), '*')
                print('*' * 36)
                for key, value in bank_Agr[account].items():
                    if key == '状态':
                        if value != '冻结':
                            print('     ', key, ':', '正常')
                        else:
                            print('     ', key, ':', value)
                    if key == '地址':
                        for m, n in bank_Agr[account][key].items():
                            print('     ', m, ':', n)
                    else:
                        print(key, ':', value)

                print('*' * 36)
                break
            elif ret == 'c_a2':
                print('账号错误次数超过限制，请到柜台解冻')
                continue
            elif ret == 'c_a3':
                print('账号密码错误%d次，超过3次将冻结' % bank_Agr[account]['状态'])
            elif ret == 'c_a4':
                print('账号输入有误,请重新输入')
            else:
                pass
    elif index == '6':
        print('Bye!')
        break
    else:
        print('无效指令')
