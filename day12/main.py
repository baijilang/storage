"""
# 厨师、顾客、收银台——>类
# 蛋糕3元一个，厨师每次生产一个蛋糕可以得到1.5元
# 开始有3名厨师，4位顾客
# 每名顾客有3000元，用完为止，相当于每个顾客最多买1000个蛋糕，满足所有顾客的需求要4000个蛋糕

# 如果篮子满了（500个）所有厨师休息3秒 （厨师的每个线程休息）
# 如果篮子空了，所有顾客休息4秒

# 假设生产3000个蛋糕就停止了，看厨师谁生产的多，顾客谁抢购的多
"""

import time, threading

# from threading import Thread

aimF = 3000  # 实际生产的指标
aim = aimF -2  # 传入的指标，
sum = 0  # 某一时刻已经生产的蛋糕
basket = 0
lock = threading.Lock()


class Chef(threading.Thread):
    name = ''
    salary = 0
    count = 0
    end = [0, ]
    status = True

    def run(self):
        global basket, sum, aim
        while True:
            if basket < 500 and sum < aim and self.status is True:
                lock.acquire()
                basket += 1
                lock.release()
                print(self.name, '又做了1个蛋糕，已经做了', self.count, '个')
                lock.acquire()
                sum += 1
                lock.release()
                self.count += 1
            elif basket == 500 and sum < aim and self.status is True:
                time.sleep(1)
            elif sum >= aim and self.status is True:
                self.salary = self.count * 1.5
                self.status = False
                lock.acquire()
                Chef.end[0] += 1
                lock.release()
            else:
                pass
                # print('姓名：%s，数量：%s，工资：%s，篮子：%s，总数：%s,状态：%s' % (self.name,self.count,self.salary,basket,sum,self.status))
            if Chef.end[0] == 3 and Customer.end[0] == 4:
                lock.acquire()
                print('%s制作了%s个蛋糕，薪水为%s元' % (self.name, self.count, self.salary))
                lock.release()
                break
            else:
                pass

    pass


class Customer(threading.Thread):
    name = ''
    balance = 3000
    count = 0
    end = [0, ]
    status = True

    def run(self):
        global basket
        while True:
            if self.balance >= 3 and basket > 0 and self.status is True:
                lock.acquire()
                basket -= 1
                lock.release()
                self.count += 1
                self.balance -= 3
                print(self.name, '抢购了1个蛋糕,已经买了', self.count, '个')
            elif self.balance >= 3 and basket == 0 and sum < aim and self.status is True:  # 暂停
                time.sleep(1)
            elif (self.balance < 3 or (basket <= 0 and sum >= aim)) and self.status is True:
                lock.acquire()
                Customer.end[0] += 1
                lock.release()
                self.status = False
            else:
               pass
                # print('姓名：%s，数量：%s，工资：%s，篮子：%s，总数：%s' % (self.name,self.count,self.balance,basket,sum))
            if Chef.end[0] == 3 and Customer.end[0] == 4 :
                lock.acquire()
                print('%s买到了%s个,还剩下%s元' % (self.name, self.count， self.balance))
                lock.release()
                break
            else:
                pass

    pass


chef1 = Chef()
chef1.name = '王师傅'
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
# customer5 = Customer()
# customer5.name = '铁柱'
# customer6 = Customer()
# customer6.name = '翠花'

chef1.start()
chef2.start()
chef3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
# customer5.start()
# customer6.start()
