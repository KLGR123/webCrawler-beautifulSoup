from pymysql import *
import json

def connectDB():
    #先创建好数据库 记住数据库名
    dbase = connect("127.0.0.1", "root", "输入密码", "数据库名")
    return dbase

def createTable(dbase):
    #获取cursor对象
    cursor = dbase.cursor()
    #sql语句语法
    sql = '''
    CREATE TABLE info
    (
    id INT PRIMARY KEY  NOT NULL,
    name    TEXT   NOT NULL,
    age      INT   NOT NULL,
    address  CHAR(50),
    salary  REAL
    );
    '''
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
    return False

def insertRecords(dbase):
    cursor = dbase.cursor()
    try:
        cursor.execute('DELETE FROM info')

        cursor.execute("INSERT INTO info (id, name ,age, address, salary) \
                        VALUES (1, 'Paul', 32, 'California', 20000.00)");
        cursor.execute("INSERT INTO info (id, name ,age, address, salary) \
                        VALUES (2, 'Allen', 25, 'Texas', 15000.00)");
        cursor.execute("INSERT INTO info (id, name ,age, address, salary) \
                        VALUES (3, 'Teddy', 23, 'Norway', 30000.00)");
        cursor.execute("INSERT INTO info (id, name ,age, address, salary) \
                        VALUES (4, 'Mark', 26, 'Paris', 12000.00)");

        db.commit()
        return True
    except:
        db.rollback()
    return False

def selectRecords(dbase):
    cursor = dbase.cursor()
    sql = 'SELECT name,age,salary FROM info ORDER BY age DESC'
    cursor.execute(sql)

    #调用fetchall方法可以获取cursor对象的全部的记录
    results = cursor.fetchall()
    print(results)

    fields = ['name', 'age', 'salary']
    records = []
    for row in results:
        #zip方法把fields序列和row(即table里面的行数据)构建联系 然后转化为字典
        #相当于records序列的元素是字典
        records.append(dict(zip(fields, row)))
    #转成json格式
    return json.dumps(records)

if __name__ == '__main__':
    db = connectDB()

    if createTable(db):
        print('成功创建info表格')
    else:
        print('创建失败或者已经存在')

    if insertRecords(db):
        print("插入数据成功")
    else:
        print('插入数据失败')

    print(selectRecords(db))
    db.close()


