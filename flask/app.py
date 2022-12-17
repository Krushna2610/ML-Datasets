import pymysql
from flask import Flask, redirect,render_template,request, url_for
db_connection=None
db_cursor=None
app = Flask(__name__)
from dbOperation import *


@app.route("/")
def index():
    # return "hello python"
    allData = getAllStudents()
    return render_template("index.html",data=allData)

@app.route("/add",methods=["GET","POST"])
def addStudent():  
    if request.method == "POST":
        data = request.form
        isInserted = insertStudent(data["name"],data["book_name"],data["phone"])
        if(isInserted):
            return redirect(url_for("index"))
        
    return render_template("add.html")

@app.route("/update",methods=["GET","POST"])
def update():
    id=request.args.get("ID",type=int,default=1)
    print(id)
    actual_data = getStudentById(id)   
    #print(actual_data)
    
    if request.method=="POST":
        data=request.form
        print("data----->",data)
        isUpdated=updateStudent(data["name"],data["book_name"],data["phone"],id) 
        if(isUpdated): 
            return redirect(url_for("index")) 
    return render_template("update.html",data=actual_data)


@app.route("/delete")
def delete():
    id=request.args.get("ID",type=int,default=1)
    isDeleted=deleteStudent(id) 
    if(isDeleted): 
        return redirect(url_for("index")) 
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True)
