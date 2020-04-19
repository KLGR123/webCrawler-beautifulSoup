from pymysql import *
import json

def connectDB():
    #�ȴ��������ݿ� ��ס���ݿ���
    dbase = connect("127.0.0.1", "root", "��������", "���ݿ���")
    return dbase

def createTable(dbase):
    #��ȡcursor����
    cursor = dbase.cursor()
    #sql����﷨
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

    #����fetchall�������Ի�ȡcursor�����ȫ���ļ�¼
    results = cursor.fetchall()
    print(results)

    fields = ['name', 'age', 'salary']
    records = []
    for row in results:
        #zip������fields���к�row(��table�����������)������ϵ Ȼ��ת��Ϊ�ֵ�
        #�൱��records���е�Ԫ�����ֵ�
        records.append(dict(zip(fields, row)))
    #ת��json��ʽ
    return json.dumps(records)

if __name__ == '__main__':
    db = connectDB()

    if createTable(db):
        print('�ɹ�����info���')
    else:
        print('����ʧ�ܻ����Ѿ�����')

    if insertRecords(db):
        print("�������ݳɹ�")
    else:
        print('��������ʧ��')

    print(selectRecords(db))
    db.close()


