from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
import mysql.connector
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Virtualization_project'
 
mysql = MySQL(app)
 
@app.route('/', methods=['POST','GET'])
def home_page():
    if request.method == 'POST':
        task_name = request.form["name"]
        task_date = request.form["date"]
        details = request.form["details"]
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""INSERT INTO Virtualization_project.todo_list (task_name,task_date,details) 
                              VALUES (%s,%s,%s)""",(task_name,task_date,details))
            mysql.connection.commit()
            cursor.close()
            return render_template('page.html')
        except:
            return "There was an issue"
    else:
        return render_template('page.html')
    #testing123
    #testing again

if __name__ == '__main__':
    app.run(debug = True,host='localhost', port=9999) 