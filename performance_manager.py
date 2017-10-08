import matplotlib.pyplot as plt
import numpy as np
import pymysql

class Performance_Man:
    def plotter(self,name):
        conn=pymysql.connect(host='localhost',user='root',password='',db='hackathon')
        a=conn.cursor()
        name="Harshit"
        sql = 'select sem from stud_pers_info where name = "{}"'.format(name)
        a.execute(sql)
        sem = a.fetchone()
        print(sem[0])

        sql= 'select sub_name from subjects where semester={}'.format(sem[0])
        a.execute(sql)
        sub1=a.fetchall()
        mks=[[],[],[]]
        per=[[],[],[]]
        sql= 'select * from marks where exam_name="ut1"'
        a.execute(sql)
        countrow=a.execute(sql)
        count=0

        sub=[]
        if(len(sub1)!=0):
          for i in range(0,len(sub1)):
             sub.append(sub1[i][0])

        if(countrow>0):
            count=1
            for i in sub:
                sql='select sub_id from subjects where sub_name="{}"'.format(i)
                a.execute(sql)
                id=a.fetchone()
                sql='select marks from marks where sub_id="{}" and exam_name="ut1" '.format(id[0])
                a.execute(sql)
                temp=a.fetchone()
                mks[0].append(temp)
                per[0].append(temp[0]/20*100)

        sql= 'select * from marks where exam_name="ut2"'
        a.execute(sql)
        countrow=a.execute(sql)
        if(countrow>0):
            count=2
            for i in sub:
                sql='select sub_id from subjects where sub_name="{}"'.format(i)
                a.execute(sql)
                id=a.fetchone()
                sql='select marks from marks where sub_id="{}" and exam_name="ut2" '.format(id[0])
                a.execute(sql)
                temp=a.fetchone()
                mks[1].append(temp[0])
                per[1].append(temp[0]/20*100)

        sql= 'select * from marks where exam_name="prelim"'
        a.execute(sql)
        countrow=a.execute(sql)
        if(countrow>0):
            count=3
            for i in sub:
                sql='select sub_id from subjects where sub_name="{}"'.format(i)
                a.execute(sql)
                id=a.fetchone()
                sql='select marks from marks where sub_id="{}" and exam_name="prelim" '.format(id[0])
                a.execute(sql)
                temp=a.fetchone()
                mks[2].append(temp[0])
                per[2].append(temp[0]/80*100)

        x=[[],[],[],[],[],[]]
        for i in range(0,len(sub)):
            for j in range(len(per)):
                if(len(per[j])!=0):
                 x[i].append(per[j][i])

        def gr(x):
           plt.gca().set_color_cycle(['red', 'green', 'blue', 'orange','black','cyan'])
           for i in range(0,len(sub)):
               plt.plot(x[i])

           plt.ylabel('PERCENTAGE')
           plt.xlabel('EXAM')
           plt.legend(sub,loc='upper left')
           plt.xticks([0,1,2],['ut1','ut2','prelim'])
           plt.ylim(0,150)
           plt.show()


        def gr1(x):
           plt.gca().set_color_cycle(['red', 'green', 'blue', 'orange','black','cyan'])
           for i in range(0,len(sub)):
               plt.plot(x[i],'*')

           plt.ylabel('PERCENTAGE')
           plt.xlabel('EXAM')
           plt.legend(sub,loc='upper left')
           plt.xticks([0,1,2],['ut1','ut2','prelim'])
           plt.ylim(0,150)
           plt.show()

        if(count==1):
            gr1(x)

        else:
            gr(x)
