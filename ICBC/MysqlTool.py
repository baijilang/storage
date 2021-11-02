import pymysql


class MysqlTool:
    def __init__(self, host='localhost', user='root', password='root'):
        self.host = host
        self.user = user
        self.password = password
        self.database = ''
        self.con = ''
        self.cursor = ''

    def creatDatbase(self, database):
        try:
            con = pymysql.connect(host=self.host, user=self.user, password=self.password)
            cursor = con.cursor()
            sql1 = 'create database if not exists %s character set utf8;'
            param1 = database
            cursor.execute(sql1 % param1)
            con.commit()
            cursor.close()
            con.close()
        except Exception as e:
            print('error:', e)
        self.database = database
        return self.database

    def creatable(self, tablename, param):
        sql = 'create table if not exists %s (%s);' % (tablename, param)
        self.connect()
        self.cursor.execute(sql)
        self.con.commit()
        self.close()
        return tablename

    def connect(self):
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def regular(self, sql, param=()):
        try:
            self.connect()
            self.cursor.execute(sql, param)
            self.con.commit()
            self.close()
        except Exception as e:
            print('error:', e)

    def search(self, sql, param=()):
        try:
            self.connect()
            self.cursor.execute(sql, param)
            ret = self.cursor.fetchall()
            self.close()
            return ret
        except Exception as e:
            print('error', e)


# con1 = MysqlTool()
# con1.creatDatbase('test_11_2')
# print(con1.database)
# sql = 'create table if not exists %s(usena varchar(10))' % 'day1'
# con1.regular(sql)
# sql1 = 'insert into day1 value(%s)'
# param1 = 'lihua'
# con1.regular(sql1,param1)
# sql2 = 'select * from day1 where usena = %s'
# param2 = 'lihua'
# print(con1.search(sql2,param2)[0][0])
#
# param3 = 'username char(10), account int(6) ,pwd varchar(6) , banlance decimal(14,2) ,' \
#          'country varchar(10),province varchar(10),street varchar(10),tablet varchar(10),' \
#          'registime timestamp'
# # sql3 = 'create table if not exists %s (%s);' % ('day3', param3)
# # print(sql3)
# con1.creatable('day3',param3)

