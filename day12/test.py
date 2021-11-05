import time


tes = True
count = 0
a = time.time()
def run():
    global tes, count
    while tes is True:
        for i in range(10):
            print(i)
        count +=1
        print('第%s次循环' % count)
        if count == 10:
            tes = False
            b = time.time()
            c = b - a
            print('结束,运行时间为：%s' % c)


run()


'''
# 厨师、顾客、收银台——>类
# 蛋糕3元一个，厨师每次生产一个蛋糕可以得到1.5元
# 开始有3名厨师，6位顾客
# 每名顾客有3000元，用完为止

# 如果篮子满了（500个）所有厨师休息3秒 （厨师的每个线程休息）
# 如果篮子空了，所有顾客休息4秒
'''


import time
from threading import Thread

aim = 6000
sum = 0
basket = 0


class Chef(Thread):
    chef_status = [True]   # 可变序列使得字类的改变可以影响父类
    chef_pause = [0.00,]
    chef_start = [0.00,]
    chef_elapse = [0.0,]
    name = ''
    salary = 0
    count = 0

    def run(self):
        global basket, sum, aim, chefstatus
        while True:
            Customer.cus_elapse[0] = Customer.cus_start[0] - Customer.cus_pause[0]
            print(Customer.cus_elapse[0])
            if Customer.cus_status[0] == False and Customer.cus_elapse[0] >= 1:  # 顾客等待时间超过1s，继续开始购物
                Customer.cus_status[0] = True
            if self.chef_status[0] == True:
                if basket < 500 and sum < aim:
                    basket+=1
                    sum +=1
                    self.count +=1
                    print(self.name,'又做了1个蛋糕，已经做了',self.count,'个')
                    print('篮子里面有',basket,'个')
                    print('顾客目前是%s，休息了%s，' % (Customer.cus_status,Customer.cus_elapse))
                    continue
                elif basket == 500 and sum < aim:
                    self.chef_status[0] = False   # 篮子满了，休息一下
                    self.chef_pause[0] = time.time()
                else:
                    counter.outcomt = counter.income - self.count * 1.5
                    self.salary = self.count * 1.5
                    print('%s制作了%s个蛋糕，薪水为%s元' % (self.name,self.count,self.salary))
                    break
                Customer.cus_start[0] = time.time()
                print(Customer.cus_start[0],Customer.cus_pause[0])
            else:
                continue
    pass


class Customer(Thread):
    cus_status = [True]
    cus_pause = [0.00,]
    cus_start = [0.00,]
    cus_elapse = [(cus_start[0] - cus_pause[0]),]
    name = ''
    balance = 3000
    count = 0

    def run(self):
        global basket
        while True:
            Chef.chef_elapse[0] = Chef.chef_start[0] - Chef.chef_pause[0]
            if Chef.chef_status[0] == False and Chef.chef_elapse[0] >= 1:  # 厨师的休息时间超过1秒
                Chef.chef_status[0] = True
            if Customer.cus_status[0] == True:
                if self.balance >= 3 and basket > 0:
                    basket -= 1
                    self.balance -= 3
                    self.count += 1
                    counter.income += 3
                    print(self.name,'抢购了1个蛋糕,已经买了',self.count,'个')
                    continue
                elif self.balance >= 3 and basket == 0: # 暂停
                    Customer.cus_pause[0] = time.time()
                    Customer.cus_status[0] = False
                else:
                    print(self.name,'的钱花完了,停止了购物！')   # 剩下的金额不足，购买停止
                    break
                Chef.chef_start[0] = time.time()
            else:
                continue

class Counter():
        income = 0
        outcomt = 0
        balance = income - outcomt
        pass


counter = Counter()
chef1 = Chef()
chef1.name = '王刚'
chef2 = Chef()
chef2.name = '赵师傅'
chef3 = Chef()
chef3.name = '叶师傅'
customer1 = Customer()
customer1.name = '张三'
customer2 = Customer()
customer2.name = '李四'
customer3 = Customer()
customer3.name = '王二'
customer4 = Customer()
customer4.name = '麻子'
customer5 = Customer()
customer5.name = '铁柱'
customer6 = Customer()
customer6.name = '翠花'

chef1.start()
chef2.start()
chef3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
customer5.start()
customer6.start()


class Summary(threading.Thread):

    def run(self):
        print('检查状态',chef1.end)
        print(chef1.end, chef3.end, chef2.end)
        if chef1.end is True and chef2.end is True and chef3.end is True:
            if customer1.end is True and customer2.end is True and customer3.end is True :
                if customer4.end is True and customer5.end is True and customer6.end is True:
                    info = '''
                    {}做了{}个蛋糕，收入{}元，
                     {}做了{}个蛋糕，收入{}元
                      {}做了{}个蛋糕，收入{}元
                    {}买了{}个蛋糕，花费{}元
                     {}买了{}个蛋糕，花费{}元
                      {}买了{}个蛋糕，花费{}元
                       {}买了{}个蛋糕，花费{}元
                        {}买了{}个蛋糕，花费{}元
                         {}买了{}个蛋糕，花费{}元
                    '''
                    param = (chef1.name, chef1.count, chef1.salary,
                             chef2.name, chef2.count, chef2.salary,
                             chef3.name, chef3.count, chef3.salary,
                             customer1.name, customer1.count, customer1.count * 3,
                             customer2.name, customer2.count, customer2.count * 3,
                             customer3.name, customer3.count, customer3.count * 3,
                             customer4.name, customer4.count, customer4.count * 3,
                             customer5.name, customer5.count, customer5.count * 3,
                             customer6.name, customer6.count, customer6.count * 3,)
                    print(info.format(param))
                else:
                    pass
            else:
                pass
        else:
            pass

    pass