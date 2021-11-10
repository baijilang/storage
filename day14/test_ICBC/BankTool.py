from MysqlTool import MysqlTool
import random


class Bank:
    __userdatesql = ' account varchar(6), level varchar(2),username char(10),' \
                    'password varchar(6) , banlance decimal(14,2) ,country varchar(10),' \
                    'province varchar(10),street varchar(10),tablet varchar(10),registime timestamp not null default now()'
    __usertable = 'userdata'

    def __init__(self, name='工商银行', limit=100):
        self.__bankname = name
        self.__database = ''
        self.__limit = limit
        self.__pymysql = MysqlTool()
        self.__database = self.__pymysql.creatDatbase(name)
        self.__usertable = self.__pymysql.creatable(self.__usertable, self.__userdatesql)

    def homepage(self):
        info = '*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*\n*{}*'
        print(info.format('*' * 30, self.__bankname.center(27, ' '),
                          '*' * 30, '选项'.center(29, ' '),
                          '1、开户'.center(28, ' '),
                          '2、存款'.center(28, ' '),
                          '3、取款'.center(28, ' '),
                          '4、转账'.center(28, ' '),
                          '5、查询'.center(28, ' '),
                          '6、Bye！'.center(29, ' '), '*' * 30, ))

    def count(self):
        self.__pymysql.connect()
        sql = 'select count(*) as num from %s ' % self.__usertable
        self.__pymysql.cursor.execute(sql)
        ret = self.__pymysql.cursor.fetchall()
        if ret[0][0] < self.__limit:
            return 1
        else:
            return 2

    def run(self, sql):
        try:
            self.__pymysql.regular(sql)
        except Exception as e:
            print('error:', e)

    def get_account(self):
        # 创建账号
        while True:
            account = ''
            for i in range(6):
                a = str(random.choice(range(10)))
                account += a
            a = self.check(account, '1')
            if a == 3:
                break
            else:
                continue
        return account

    def addUser(self, account, username, level, password, country, province, street, tablet):
        r1 = self.count()
        # 账号在外部生成，但不提交到数据库
        if r1 == 2:
            return 2  # 数据库已满
        if username == '':
            return 3  # 名字为空
        if level not in ['1', '2']:
            return 4  # 不符合规范的卡种
        if len(password) != 6:
            return 5  # 密码不是6位
        if not password.isdigit():
            return 6  # 密码包含除了数字外的字符
        if country == '' or province == '' or street == '' or tablet == '':
            return 7  # 地址未填写完整
        try:
            param = (self.__usertable, (account, level, username, password, 0.00, country, province, street, tablet))
            sql = 'insert into %s (account,level,username,password,balance,country,province,street,tablet) value%s' % param
            self.run(sql)
            return 1
        except Exception as e:
            print('error:', e)
            return 8  # 数据库连接错误

    def savemoney(self, account, money):
        ret = self.check(account, 1)
        money = str(money)
        if ret == 3:
            return 3  # 账号错误
        if not money.replace('.', '').isdigit():
            return 2  # 金额错误
        if float(money) < 0:
            return 2
        money = float(money)
        sql = 'update %s set balance=%s+balance where account=%s' % (self.__usertable, money, account)
        self.run(sql)
        return 1

    def getmoney(self, account, password, money):
        ret = self.check(account, password)
        money = str(money)
        if ret == 3:
            return 3, 0  # 账号错误
        if ret == 2:
            return 2, 0  # 密码错误
        if not money.replace('.', '').isdigit():
            return 4, 0  # 金额输入错误
        if float(money)<0:
            return 4,0
        sqls = 'select balance from %s where account=%s' % (self.__usertable, account)
        ret = self.__pymysql.search(sqls)
        if ret[0][0] >= float(money):
            sql = 'update %s set balance=balance-%s where account=%s' % (self.__usertable, money, account)
            self.run(sql)
            return 1, ret[0][0]
        else:
            return 5, ret[0][0]

    def transmoney(self, account_out, password_out, account_in, money):
        a = self.check(account_out, password_out)
        b = self.check(account_in, 1)
        money = str(money)
        if a != 1:
            return 2  # print('转出账号或密码错误')
        if b == 3:
            return 3  # print('转入账号错误')
        if not (money.isdigit() or (money.replace('.', '').isdigit()) and money.count('.') == 1):
            return 4  # 金额输入不符合要求
        if float(money) < 0:
            return 4
        money = float(money)
        ret = self.getinfo(account_out)
        if ret[0][1] == '1' and money > 20000:
            return 5  # print('Ⅰ类卡单次转账不能超过2万元')
        if ret[0][1] == '2' and money > 50000:
            return 6  # print('Ⅱ类卡单次转账不能超过5万元')
        self.getmoney(account_out, password_out, money)
        self.savemoney(account_in, money)
        return 1

    def check(self, account, pwd):
        account = str(account)
        if not account.isdigit() or len(account) != 6:
            return 3
        self.__pymysql.connect()
        sql = 'select password from %s where account=%s' % (self.__usertable, account)
        self.__pymysql.cursor.execute(sql)
        ret = self.__pymysql.cursor.fetchall()
        self.__pymysql.close()
        if len(ret) == 1:
            if ret[0][0] == pwd:
                return 1
            else:
                return 2  # 账号存在，密码错误
        else:
            return 3  # 账号错误

    def getinfo(self, account):
        try:
            sql = 'select * from %s where account=%s' % (self.__usertable, account)
            self.__pymysql.connect()
            self.__pymysql.cursor.execute(sql)
            ret = self.__pymysql.cursor.fetchall()
            return ret
        except Exception as e:
            print('error:', e)

    def add(self):
        account = self.get_account()
        username = input('姓名:')
        level = input('卡类:')
        password = input('密码:')
        country = input('国家:')
        province = input('省份:')
        street = input('街道:')
        tablet = input('门牌号:')

        result = self.addUser(account, username, level, password, country, province, street, tablet)
        if result == 1:
            ret = self.getinfo(account)
            print('开户成功，请牢记您的账户信息')
            list = []
            for i in ret[0]:
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
        elif result == 2:
            print('开户失败，数据库已满！！！')
        elif result == 3:
            print('姓名为空！！！')
        elif result == 4:
            print('不符合规范的卡种！！！')
        elif result == 5:
            print('密码不是6位数字！！！')
        elif result == 6:
            print('密码包含除数字外的字符！！！')
        elif result == 7:
            print('地址未填写完整！！！')

    def save_money(self):
        account = input('请输入存款账号：')
        ret = self.check(account, 1)
        if ret == 2:
            money = input('请输入金额：')
            if type(eval(money)) is float or int:
                a = self.savemoney(account, money)
                if a == 1:
                    print('存款成功')
                else:
                    print('存款失败')
            else:
                print('#金额输入格式不正确#')
        else:
            print('#账号有误#')

    def get_money(self):
        account = input('请输入取款账号：')
        password = input('请输入取款密码：')
        money = input('请输入金额：')
        a, b = self.getmoney(account, password, money)
        if a == 1:
            balance = float(b) - float(money)
            print('取款成功!当前账户余额：{:.2f}元'.format(balance))
        elif a == 4:
            print('#金额输入格式不正确#')
        elif a == 5:
            print('余额不足，取款失败!当前余额为%s' % b)
        else:
            print('账号或密码错误')
        pass

    def trans_money(self):
        print('当前版本仅支持本行间转账业务')
        account_out = input('请输入转账账号：')
        password_out = input('请输入转账密码：')
        account_in = input('请输入收款账号：')
        money = input('请输入金额：')
        ret = self.transmoney(account_out, password_out, account_in, money)
        if ret == 1:
            print('转账成功')
            info = self.getinfo(account_out)
            print('当前账户余额为：', info[0][4], '元')
        if ret == 2:
            print('转出账号或密码错误')
        if ret == 3:
            print('转入账号错误')
        if ret == 4:
            print('金额输入不符合要求')
        if ret == 5:
            print('Ⅰ类卡单次转账不能超过2万元')
        if ret == 6:
            print('Ⅱ类卡单次转账不能超过5万元')

    def search_info(self):
        account = input('请输入查询账号：')
        password = input('请输入查询密码：')
        ret = self.check(account, password)
        if ret == 1:
            retinfo = self.getinfo(account)
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
        else:
            print('账号或秘密有误')

    pass
