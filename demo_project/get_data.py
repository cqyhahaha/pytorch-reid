import mysql.connector
import time

def db_connection():
    mydb = mysql.connector.connect( host = '192.168.1.100',
    user = 'cqy',
    port = '3306',
    database = 'edgedemo',
    passwd = '123456',
    autocommit = True)
    return mydb

mydb = db_connection()
cur = mydb.cursor()
print("Opened database successfully")

p1 = "Person_1"
p2 = "Person_2"
c1 = 1
c2 = 2
c3 = 3

sql1 = "insert into REID(person,ctime, camera) values ('{0}',{1},{2})".format(str(p1), int(time.time()), c1)
print(sql1)
cur.execute(sql1)

time.sleep(1)

sql2 = "insert into REID(person,ctime, camera) values ('{0}',{1},{2})".format(str(p1), int(time.time()), c3)
print(sql2)
cur.execute(sql2)

time.sleep(1)

sql3 = "insert into REID(person,ctime, camera) values ('{0}',{1},{2})".format(str(p1), int(time.time()), c2)
print(sql3)
cur.execute(sql3)




cur.execute("select * from REID")

datas = cur.fetchall()
for data in datas:
	print(data)

#cur.execute("DROP TABLE REID")
mydb.close()	
