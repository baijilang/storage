import xlrd


def create_table():
    import pymysql
    con = pymysql.connect(host='localhost', user='root', password='root', database='cloth_data')
    cursor = con.cursor()
    pn = 'sales_data'
    pm = '`month` varchar(4)'
    p1 = '`date` VARCHAR(6)'
    p2 = 'clo_name VARCHAR(20)'
    p3 = 'price DECIMAL(10,2)'
    p4 = 'store SMALLINT'
    p5 = 'amounts SMALLINT'
    param = (pn,pm, p1, p2, p3, p4, p5)
    sql = ('create table %s(%s,%s,%s,%s,%s,%s);' % param)
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()


def insert(sql, param):
    import pymysql
    con = pymysql.connect(host='localhost', user='root', password='root', database='cloth_data')
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()
    return 1

create_table()

excel = xlrd.open_workbook(filename=r'2020年每个月的销售情况.xlsx', encoding_override=True)
for i in excel.sheet_names():
    sheet = excel.sheet_by_name(i)
    mon = i
    row = sheet.nrows
    for num in range(1,row):
        row_value = sheet.row_values(num)
        param = [mon]+row_value[0:5]
        sql = 'insert into sales_data values(%s,%s,%s,%s,%s,%s);'
        insert(sql, param)
        pass
    pass
pass
