# a)用户：账号（str：系统随机产生8位数字）、姓名(str)、密码(int:6位数字)、存款余额(int)、
# 地址、开户行（银行的名称（str））写死的！
# b)地址：国家(str)、省份(str)、街道(str)、门牌号(str)
#首页面显示
print('*'*41)
print('*','中 国 工 商 银 行'.center(33,' '),'*')
print('*','账 户 管 理 系 统'.center(33,' '),'*')
print('*','V 1.0'.center(37,' '),'*')
print('*'*41)
print('*','%-35s' % '1、开户','*')
print('*','%-35s' % '2、存钱','*')
print('*','%-35s' % '3、取钱','*')
print('*','%-35s' % '4、转账','*')
print('*','%-35s' % '5、查询','*')
print('*','%-36s' % '6、Bye!','*')
print('*','%-34s' % '0、返回上级','*')
###创建字典/读取字典
bank = {None:{'姓名':None,
              '密码':[None,0],
              '余额':None,
              '银行':'中国工商银行',
              '地址': {'国家':None,'省份':None, '街道':None, '门牌号':None}}}
#定义操作函数  分别为添加操作，账号核对操作，余额计算操作
import random


def open_account(account):
    bank_tem=[]
    if account not in bank_tem:
        name=input('请输入姓名：')
        while True:
            password=input('请输入6位数字密码：')
            if password.isdigit() and len(password) == 6:
                break
            else:print('格式不正确')
        money=0
        bank='中国工商银行'
        country=input('请输入国家：')
        province=input('请输入省份：')
        street=input('请输入街道：')
        door=input('请输入门牌号：')
        bank_tem={account:{'姓名':name,
              '密码':[password,0],
              '余额':money,
              '银行':'中国工商银行',
              '地址': {'国家':country,'省份':province, '街道':street, '门牌号':door}}}
        return bank_tem  #
def account_password(account,password):   #判断输入账号密码是否存在、匹配：
    result = [False,None,None]
    if account.isdigit() and len(account) == 8:
        if bank[account]['密码'][1] == '冻结':
            print('该账号已冻结')
        elif account in bank and bank[account]['密码'][1] != 3:
            if password == bank[account]['密码'][0] and password!=0:
                bank[account]['密码'][1] = 0
                result=[True,account,password]
                print('请稍等……')
                return result
            elif bank[account]['密码'][1] < 2 and password!=0:
                bank[account]['密码'][1] += 1
                print('密码错误%d次' % bank[account]['密码'][1])
            elif password == '0':
                print('退出成功')
            else:      # bank[account][password][1] == 3 and password!=0:
                bank[account]['密码'][1] += 1
                print('密码错误%d次,账号冻结' % bank[account]['密码'][1])
                bank[account]['密码'][1] = '冻结'

        else: print('该账号不存在')
    else:
        print('该账号不存在')
    return result
def change_money(account,password,way):  #way根据存款或取款不同，分别取1或-1
    while True:
        money_deposit=input('请输入金额,结束操作请输入0：')
        if (money_deposit.isdigit() or money_deposit.count('.') == 1) and money_deposit != '0':
            a = bank[account]['余额']
            bank[account]['余额'] += way*float(money_deposit)
            if bank[account]['余额']>= 0 :
                print('操作结束，您当前余额为%.2f' % (bank[account]['余额']))
            else:
                print('操作失败，您当前余额为%.2f' % a)
        elif money_deposit == '0':
            print('操作结束' )
            break
        else:print('请输入数字')


while True:
    index=input('请选择您要办理的业务：')
    if index == '1':
        if len(bank) <= 100:
            rannum = []
            for i in range(0, 8):
                rannum.append(random.choice('1234567890'))
            account = ''.join(rannum)
            print('创建账号：',account)
            if account not in bank:
                bank.update(open_account(account))            #创建账号完成
                # for key,value in bank[account].items():   遍历账号信息
                #     print(key,  value)
                info='''
开户成功!
————————————————————————————————————
%s账号:%-30s%s                  
%s姓名:%-30s%s 
%s密码:%-30s%s 
%s余额:%-30s%s 
%s开户银行:%-22s%s 
%s地址:%-30s%s 
%s    国家:%-26s%s 
%s    省份:%-26s%s 
%s    街道:%-26s%s 
%s    门牌号:%-24s%s 
————————————————————————————————————
'''
                print(info % ('|',account,'|','|',bank[account]['姓名'],'|','|','******','|','|','0.00','|','|','中国工商银行','|','|','——','|','|',
                              bank[account]['地址']['国家'],'|','|',bank[account]['地址']['省份'],'|','|',
                              bank[account]['地址']['街道'],'|','|',bank[account]['地址']['门牌号'],'|'))
        else:print('用户已满')

    elif index == '2':
        while True:
            account = input('请输入账号：')
            if account == '0':
                print('退出成功')
                break
            password = bank[account]['密码'][0]
            a=account_password(account,password)
            if a[0]==True:
                change_money(a[1],a[2],1)
                break
            else:
                continue

    elif index == '3':
        while True:
            account = input('请输入账号：')
            if account == '0':
                print('退出成功')
                break
            password = input('请输入密码：')
            if password == '0':
                print('退出成功')
                break
            a = account_password(account, password)
            if a[0] == True:
                change_money(a[1], a[2], -1)
                break
            else:
                continue

    elif index == '4':
        while True:
            account_out = input('请输入付款账号：')
            if account_out == '0':
                print('退出成功')
                break
            password_out = input('请输入付款账号密码：')
            if password_out == '0':
                print('退出成功')
                break
                ######以上是付款账号的账户与密码，以下判断付款账户的账号  03522416   10533322
            account_in = input('请输入收款账号：')
            if account_in == '0':
                print('退出成功')
                break
            password_in = bank[account_in]['密码'][0]
            a = account_password(account_out, password_out)
            b = account_password(account_in, password_in)
            if a[0] == True and b[0] == True:
                origin_out=bank[account_out]['余额']
                change_money(a[1], a[2], -1)
                bank[account_in]['余额']=bank[account_in]['余额']+(origin_out - bank[account_out]['余额'])
                break
            else:
                continue
    elif index == '5':
        while True:
            account = input('请输入查询账号：')
            if account == '0':
                print('退出成功')
                break
            password = input('请输入密码：')
            if password == '0':
                print('退出成功')
                break
            a = account_password(account, password)
            if a[0] == True:
                for key,value in bank[account].items():
                    print(key,  value)
    elif index == '6':
        print('Bye!')
        break
