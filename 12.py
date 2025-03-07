import sqlite3
db=sqlite3.connect('test.db')
print("Database Operations:\n 1.Create database \n 2.Insert \n 3.Update \n 4.Delete \n 5.Select \n 6.Exit \n")
def create():
    cur=db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS student5(
regno INTEGER PRIMARY KEY,
name TEXT(40) NOT NULL,
age INTEGER,
percentage REAL);''')
    print('table created successfully')

def insert():
    db=sqlite3.connect('test.db')
    regno=int(input("Enter register number:"))
    name=input("Enter student name:")
    age=int(input("Enter age:"))
    percentage=float(input("Enter percentage:"))
    qry="insert into student5 values(%d,'%s',%d,%f)"
    cur=db.cursor()
    cur.execute(qry%(regno,name,age,percentage))
    print("Record inserted successfully")
    db.commit()
def update():
    db=sqlite3.connect('test.db')
    regno=int(input("ENter register number of the student to be updated:"))
    name=input("Enter student name:")
    age=int(input("Enter age:"))
    percentage=float(input("ENter percentage:"))
    qry="update student5 set name='%s',age=%d,percentage='%f' where regno=%d"
    cur=db.cursor()
    cur.execute(qry%(name,age,percentage,regno))
    print("Record updated successfully")
    db.commit()
def delete():
    db=sqlite3.connect('test.db')
    regno=int(input("ENter register number of the student to be deleted:"))
    qry="DELETE from student5 where regno=%d;"
    cur=db.cursor()
    cur.execute(qry%(regno))
    print("Record Deleted successfully")
    db.commit()
def select():
    db=sqlite3.connect('test.db')
    sql="SELECT * from student5;"
    cur=db.cursor()
    cur.execute(sql)
    while True:
        record=cur.fetchone()
        if record==None:
            break
        print(record)
    db.close()

while(1):
    n=int(input("Enter your choice:"))
    if n==1:
        create()
    elif n==2:
        insert()
    elif n==3:
        update()
    elif n==4:
        delete()
    elif n==5:
        select()
    elif n==6:
        print("Exited")
        break
    else:
        print("wrong choice")
    
                
