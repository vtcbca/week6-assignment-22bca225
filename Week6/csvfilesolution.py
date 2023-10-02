# 1.Create a result table which contain student id, student name and 5 subject marks.
import sqlite3 as sq
import csv
conn=sq.connect("c://sqlite3//student.db")
cur=conn.cursor()
cur.execute(" " "create table if not exists result(sid int primary key,sname text, sub1 int,sub2 int,sub3 int,sub4 int,sub5 int)""")

# 2.Enter 10 studnet details with its marks.
i1="insert into result values(?,?,?,?,?,?,?)"
l=[]
for i in range(2):
    no=int(input("Enter student id:"))
    sn=input("Enter student name:")
    sub1=int(input("Enter subject 1 marks:"))
    sub2=int(input("Enter subject 2 marks:"))
    sub3=int(input("Enter subject 3 marks:"))
    sub4=int(input("Enter subject 4 marks:"))
    sub5=int(input("Enter subject 5 marks:"))
    record=[no,sn,sub1,sub2,sub3,sub4,sub5]
    l.append(record)
    cur.executemany(i1,l)
    
# 3.Dump table into csv file "result.csv".
cur.execute('select * from result;')
r=cur.fetchall()
conn.commit()
head=['sid','sname','sub1','sub2','sub3','sub4','sub5']
with open("c:\\sqlite3\\result.csv","w",newline='') as file:
    writer=csv.writer(file)
    writer.writerow(head)
    writer.writerows(r)
    
# 4. Read result.csv file and Print Total Marks and Grade of each student. Also Append Total Marks and Grade column into result.csv file.
i=0
add=[]
with open("c:\\sqlite3\\result.csv","r") as file:
    read = csv.reader(file)
    header=next(read)
    for row in read:
        i=i+1
        print("Record{}:".format(i))
        print("id:",row[0])
        print("name:",row[1])
        print("sub1:",row[2])
        print("sub2:",row[3])
        print("sub3:",row[4])
        print("sub4:",row[5])
        print("sub5:",row[6])
        row.append(int(row[2])+int(row[3])+int(row[4])+int(row[5])+int(row[6]))
        row.append(row[7]/5)
        print("Total marks:",row[7])
        print("percentage:",row[8])
        if records[8]>80:    #Based on condition grade is assigned
                records.append('Distinction')
        elif records[8]>65 and records[8]<=80:
                records.append('First Class')
        elif records[8]>50 and records[8]<=65:
                records.append('Second Class')
        elif records[8]>35 and records[8]<=50:
                records.append('Pass')
        else:
                records.append('Fail')
        print("grade:",row[9])
        add.append(row)
with open("c:\\sqlite3\\csv\\result.csv","w") as f:
    write=csv.writer(f)
    head.extend(('total','percentage','grade'))
    write.writerow(head)
    write.write.rows(add)
    
# 5. List out Top 3 Student id and name with its percentage.
with open("c:\\sqlite3\\result.csv","r") as file:
        r=csv.reader(file)
        read=list(r)
        i=0
        L=[]
        for row in read:
            L.append(row[8])  
        L.pop(0)
        L.sort(reverse=True)     
        for per in L[:3]:        
            for list in read :
                if per in list:       
                    i=i+1
                    print("Top:",i)
                    print("ID:",list[0])
                    print("Name:",list[1])
                    print("Total:",list[7])
                    print("Percentage:",list[8])
