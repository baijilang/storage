from MysqlTool import  MysqlTool

class Bank:
    __userdatesql = ' account varchar(6), level varchar(2),username char(10),' \
                    'password varchar(6) , banlance decimal(14,2) ,country varchar(10),' \
                    'province varchar(10),street varchar(10),tablet varchar(10),registime timestamp not null default now()'
    __usertable = 'userdata'

    def __init__(self,name,limit=100):
        self.__bankname = name
        self.__database = ''
        self.__limit = limit
        self.__pymysql = MysqlTool()
        self.__database = self.__pymysql.creatDatbase(name)
        self.__usertable = self.__pymysql.creatable(self.__usertable,self.__userdatesql)

    def count(self):
        self.__pymysql.connect()
        sql = 'select count(*) as num from %s ' % self.__usertable
        self.__pymysql.cursor.execute(sql)
        ret = self.__pymysql.cursor.fetchall()
        if ret[0][0] < self.__limit:
            return 1
        else :
            return 2

    def run(self,sql):
        try:
            self.__pymysql.regular(sql)
        except Exception as e:
            print('error:', e)

    def addUser(self,account,level,username,pwd,country='',province='',street='',tablet=''):
        param = (self.__usertable,(account,level,username,pwd,0.00,country,province,street,tablet))
        print('add')
        sql = 'insert into %s (account,level,username,password,balance,country,province,street,tablet) value%s' % param
        self.run(sql)
        sqlre = 'select * from %s where account=%s' % (self.__usertable,account)
        ret = self.__pymysql.search(sqlre)
        return ret

    def savemoney(self,account,money):
        sql = 'update %s set balance=%s+balance where account=%s' % (self.__usertable,money,account)
        self.run(sql)
        print('ok')

    def getmoney(self,account,money):
        sqls = 'select balance from %s where account=%s' %(self.__usertable,account)
        ret = self.__pymysql.search(sqls)
        if ret[0][0]>=money:
            sql = 'update %s set balance=balance-%s where account=%s' % (self.__usertable,money,account)
            self.run(sql)
            return 1,ret[0][0]
        else:
            return 2,ret[0][0]

    def check(self,account,pwd):
        self.__pymysql.connect()
        sql = 'select password from %s where account=%s' % (self.__usertable,account)
        self.__pymysql.cursor.execute(sql)
        ret = self.__pymysql.cursor.fetchall()
        self.__pymysql.close()
        if len(ret)==1:
            if ret[0][0] == pwd:
                return 1
            else:
                return 2  #账号存在，密码错误
        else:
            return 3 #账号错误

    def getinfo(self,account):
        try :
            sql = 'select * from %s where account=%s' % (self.__usertable, account)
            self.__pymysql.connect()
            self.__pymysql.cursor.execute(sql)
            ret = self.__pymysql.cursor.fetchall()
            return ret
        except Exception as e:
            print('error:', e)

