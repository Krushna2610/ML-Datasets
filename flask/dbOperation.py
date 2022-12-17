import pymysql
from flask import Flask, redirect,render_template,request, url_for
db_connection=None
db_cursor=None
app = Flask(__name__)



def db_connet():
    global db_connection,db_cursor
    try:
            db_connection = pymysql.connect(host="localhost",user="root",passwd="",database="library_management_system",port=3306)
            print("Connected")
            db_cursor=db_connection.cursor()
            return True
    except:
        print("some error occure, cant connect to database")
        return False



def db_disconnect():
    global db_connection,db_cursor
    db_connection.close()
    db_cursor.close()

def getAllStudents():
    isConnected = db_connet()
    if(isConnected):
        print("yes connected")
        getQuery = "select * from students;"  #writting query
        db_cursor.execute(getQuery)           #executing query
        allData = db_cursor.fetchall()        #fetching data from query
        #print(allData)
        db_disconnect()
        return allData

def insertStudent(name,book_name,phone):
    isConnected = db_connet()
    if(isConnected):
        insertQuery = "insert into students(name,book_name,phone) values (%s,%s,%s);"  #writting query
        db_cursor.execute(insertQuery,(name,book_name,phone)) #executing query
        db_connection.commit()
        db_disconnect()
        return True
    else:
        return False

def getStudentById(id):
    isConnected = db_connet()
    if(isConnected):
        selectQuery = "select * from students where id=%s;"  #writting query
        db_cursor.execute(selectQuery,(id)) #executing query
        current_student=db_cursor.fetchone()
        db_connection.commit()
        db_disconnect()
        return current_student
    else:
        return False

def updateStudent(name,book_name,phone,id):
    isConnected = db_connet()
    if(isConnected):
        updateQuery = "update students set name=%s,book_name=%s,phone=%s where id=%s;"  #writting query
        db_cursor.execute(updateQuery,(name,book_name,phone,id)) #executing query
        db_connection.commit()
        db_disconnect()
        return True
    else:
        return False


def deleteStudent(id):
    isConnected = db_connet()
    if(isConnected):
        deleteQuery = "delete from students where id=%s ;"  #writting query
        db_cursor.execute(deleteQuery,(id)) #executing query
        db_connection.commit()
        db_disconnect()
        return True
    else:
        return False
