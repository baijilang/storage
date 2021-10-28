import pymysql


def update(sql, param):
    # 创建数据库连接
    host = 'localhost'
    user = 'root'
    password = 'root'
    database = 'bank'
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    # 创建控制台
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()
    return 1


def select(sql, param=None, fetch='all', size='1'):
    # 创建数据库连接
    host = 'localhost'
    user = 'root'
    password = 'root'
    database = 'bank'
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    # 创建控制台
    cursor = con.cursor()
    cursor.execute(sql, param)
    if fetch == 'one':
        answer = cursor.fetchone()
    elif fetch == 'all':
        answer = cursor.fetchall()
    elif cursor.fetchmany(size):
        answer = cursor.fetchmany(size)
    else:
        return 2
    cursor.close()
    con.close()
    return answer
