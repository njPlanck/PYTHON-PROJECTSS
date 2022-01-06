import psycopg2
#backend
def studentData():
  conn=psycopg2.connect(
    host='localhost',
    database='student',
    user='postgres',
    password='wizboy12'
  )
  print("Opened Successfully")
  cur = conn.cursor()
  cur.execute('''CREATE TABLE students(id INTEGER PRIMARY KEY NOT NULL,StdID VARCHAR, Firstname VARCHAR, Surname VARCHAR,DoB VARCHAR, Age VARCHAR,Gender VARCHAR,Address VARCHAR,Mobile VARCHAR);''')
  print("Table created successfully")
  conn.commit()
  conn.close()

def addStdRec(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
  conn=psycopg2.connect(
    host='localhost',
    database='student',
    user='postgres',
    password='wizboy12'
  )
  print("Opened stdREC Successfully")
  cur = conn.cursor()
  cur.execute('''INSERT INTO students VALUES(NULL,?,?,?,?,?,?,?,?)''',StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile)
  conn.commit()
  conn.close()

def viewData():
  conn=psycopg2.connect(
    host='localhost',
    database='student',
    user='postgres',
    password='wizboy12'
  )
  print("Opened stdREC Successfully")
  cur = conn.cursor()
  cur.execute('''SELECT * FROM students''')
  row = cur.fetchall()
  conn.commit()
  conn.close()
  return row


def deleteRec(id):
  conn=psycopg2.connect(
    host='localhost',
    database='student',
    user='postgres',
    password='wizboy12'
  )
  cur = conn.cursor()
  cur.execute('''DELETE FROM students WHERE id=?''',(id,))
  conn.commit()
  conn.close()

def searchData(StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
  conn=psycopg2.connect(
    host='localhost',
    database='student',
    user='postgres',
    password='wizboy12'
  )
  cur = conn.cursor()
  cur.execute('''SELECT * FROM students WHERE StdID=? OR Fristname=?,Surname=?,DoB=?,Age=?,Gender=?,Address=?,Mobile=?)''',StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile)
  row = cur.fetchall()
  conn.commit()
  conn.close()
  return row

def dataUpdate(id,StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
  conn=psycopg2.connect(
    host='localhost',
    database='student',
    user='postgres',
    password='wizboy12'
  )
  cur = conn.cursor()
  cur.execute('''INSERT INTO students VALUES(NULL,?,?,?,?,?,?,?,?)''',StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile)
  conn.commit()
  conn.close()

studentData()