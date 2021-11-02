import random
from BankTool import Bank


info = '*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*'
print(info.format('*'*30,'工商银行'.center(27,' '),
                  '*'*30,'选项'.center(29,' '),
                  '1、开户'.center(28,' '),
                  '2、存款'.center(28,' '),
                  '3、取款'.center(28,' '),
                  '4、转账'.center(28,' '),
                  '5、查询'.center(28,' '),
                  '6、Bye！'.center(29,' '),'*' * 30,))
bank = Bank('工商银行')
while True:
    index = input('请输入指令:')
    if index == '1':
        while True:
            ret = bank.count()
            if ret == 1:
                account=''
                for i in range(6):
                    a = str(random.choice(range(10)))
                    account+=a
                # account = int(account)
                a = bank.check(account,'1')
                if a == 3:
                    break
                else:
                    continue
                # bank.addUser()
            else:
                print('数据库已满')
        print(account)   #账号
        while True:
            level = input('请选择开卡种类(1 or 2):')
            if level in ['1','2']:
                break
            else:
                print('#本行暂时无此类卡，请重新选择#')
        while True:
            name = input('请输入姓名：')
            if name is None:
                print('#姓名不能为空#')
                continue
            else:break
        while True:
            password = input('请输入密码：')
            if password.isdigit() and len(password) == 6:
                break
            else:print('#格式不正确#')
        country = input('请输入国家：')
        province = input('请输入省份：')
        street = input('请输入街区：')
        tablet = input('请输入门牌号：')
        ret = bank.addUser(account,level,name,password,country,province,street,tablet)
        print('开户成功，请牢记您的账户信息')
        list = []
        for i in ret[0]:
            list.append(i)
        list[3]='******'
        info1 = '''欢迎使用工商银行
账号：{}
卡类：{}类卡
户名：{}
密码：{}
余额：{:.2f}元
地址：{}{}{}{}
开户时间：{}'''
        print(info1.format(*list))
    elif index == '2':
        account = input('请输入存款账号：')
        ret = bank.check(account,1)
        if ret == 2:
            money = input('请输入金额：')
            if type(eval(money)) is float or int:
                bank.savemoney(account,money)
                print('存款成功')
            else:
                print('#金额输入格式不正确#')
        else:
            print('#账号或密码有误#')
    elif index == '3':
        account = input('请输入取款账号：')
        password = input('请输入取款密码：')
        ret = bank.check(account,password)
        if ret == 1:
            money = input('请输入金额：')
            if type(eval(money)) is float or int:
                money = float(money)
                a, b = bank.getmoney(account, money)
                if a == 1:
                    balance = float(b) - money
                    print('取款成功!当前账户余额：{:.2f}元'.format(balance))
                    break
                else:
                    print('取款失败!当前余额为%s' % b)
                    continue
            else:
                print('#金额输入格式不正确#')
        if ret == 2 or ret == 3:
            print('#账号或密码有误#')
    elif index == '4':
        print('当前版本仅支持本行间转账业务')
        account_out = input('请输入转账账号：')
        password_out = input('请输入转账密码：')
        if account_out != '' and password_out != '':
            ret_out = bank.check(account_out, password_out)
            if ret_out == 1:
                account_in = input('请输入收款账号：')
                ret_in = bank.check(account_in,1)
                if ret_in == 2:
                    while True:
                        money = input('请输入金额：')
                        if type(eval(money)) is float or int:
                            money = float(money)
                            ret = bank.getinfo(account_out)
                            if ret[0][1] == '2' and money > 50000:
                                print('Ⅱ类卡单次转账不能超过5万元')
                                continue
                            elif ret[0][1] == '1' and money > 20000:
                                print('Ⅰ类卡单次转账不能超过2万元')
                                continue
                            else:
                                a, b = bank.getmoney(account_out, money)
                                if a == 1:
                                    bank.savemoney(account_in, money)
                                    balance = (float(b)-money)
                                    print('转账成功!当前账户余额：{:.2f}元'.format(balance))
                                    break
                                else :
                                    print('转账失败!当前余额为{:.2f}'.format(float(b)))
                                    continue
                        elif money == 'q':
                            print('已退出操作')
                            break
                        else:
                            print('#金额输入格式不正确#')
                            continue
                else:
                    print(ret_in,'#收款账户账号输入有误#')
            elif ret_out == 2 or ret_out == 3:
                print('#转账账户账号或密码输入有误#')
        else :print('#转账账户账号或密码输入有误#')
    elif index == '5':
        account = input('请输入查询账号：')
        password = input('请输入查询密码：')
        ret = bank.check(account, password)
        if ret == 1:
            retinfo = bank.getinfo(account)
            list = []
            for i in retinfo[0]:
                list.append(i)
            list[3] = '******'
            info1 = '''欢迎使用工商银行
            账号：{}
            卡类：{}类卡
            户名：{}
            密码：{}
            余额：{:.2f}元
            地址：{}{}{}{}
            开户时间：{}'''
            print(info1.format(*list))
    elif index == '6':
        break