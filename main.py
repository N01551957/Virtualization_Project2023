from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL

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

@app.route('/Display')
def Display_all_Tasks():
    """
    Function name: Display_all_students
    Developer: Joseph Keaveny
    Date: 12-10-23

    This function connects to the mysql database and returns the students in the student table
    :param connection:
    :return:
    """
    try:
        querry = "SELECT * FROM virtualization_project.todo_list ORDER BY task_date;"
        cursor = mysql.connection.cursor()
        cursor.execute(querry)
        results = cursor.fetchall()
        if results:
            return render_template('page.html', results=results)
        else:
            return render_template('page.html')
    except:
        return render_template('page.html')
    
@app.route('/Delete')
def Delete_Tasks():
    """
    Function name: Display_all_students
    Developer: Joseph Keaveny
    Date: 12-10-23

    This function connects to the mysql database and returns the students in the student table
    :param connection:
    :return:
    """
    
    cursor = mysql.connection.cursor()
    cursor.execute("""DELETE FROM virtualization_project.todo_list WHERE task_id > 1""")
    mysql.connection.commit()
    cursor.close()
    return render_template('page.html')
        
if __name__ == '__main__':
    app.run(debug = True,host='localhost', port=9999)  

#testing