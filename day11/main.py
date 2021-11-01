class Chef(object):
    __name = ''
    __age = ''

    def setAge(self, age):
        if type(age) == int and age > 0:
            self.__age = age

    def setName(self, name):
        if name is not None:
            self.__name = name

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def steam_rice(self):
        print('蒸')

    pass


class Chef11(Chef):
    def stir_fry(self):
        print('炒')

    pass


class Chef21(Chef11):
    def steam_rice(self):
        print('蒸饭')

    def stir_fry(self):
        print('炒菜')

    pass


class ChefTset(Chef11):
    pass


chef_one = ChefTset()
chef_one.setName('wanggang')
chef_one.setAge(20)
chef_one.stir_fry()
chef_one.steam_rice()

'''
i.人：年龄，性别，姓名。
ii.现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
'''


class Human(object):
    name = ''
    sex = ''
    age = ''

    def __init__(self, name, sex, age):
        self.name = name
        self.age = age
        self.sex = sex


class Worker(Human):
    job = 'worker'

    def work(self):
        print(self.name, 'is workig,she is a', self.job)


class Student(Human):
    job = 'student'
    st_num = ''

    def study(self):
        print(self.name, 'is a', self.job)

    def sing(self):
        print('students have time to sing')


people1 = Human('libai', 'male', '45')
people2 = Worker('zhangfei', 'male', '42')
people2.work()
people3 = Student('limei', 'female', '20')
people3.sing()
people3.study()
