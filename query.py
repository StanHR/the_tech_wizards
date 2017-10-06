import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='hackathon')
a = conn.cursor()
sql = ('select * from subjects')
a.execute(sql)
countrow = a.execute(sql)
print("Number of Rows: ",countrow)
for i in range(0,countrow):
    data = a.fetchone()
    print(data)