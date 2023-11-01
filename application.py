"""
Application Name: CCGC-5003 Lab 6.py
Developer: Joseph Keaveny
Date: 10/10/23

Objective:
    Create MySQL schema and tables
    Integrate Python application with MySQL schema
    Perform basic SQL operations using Python


Description:The application reads from and updates a mysql database and returns the requested information
execute_query() - takes an input and sends the command to the mysql database
read_db() - takes an input and gets info from the mysql database
display_all_students() - displays all the added students and student info
display_all_courses() - displays all the courses and course info
Display_all_registrations_students_and_courses() - displays a Joined table of registration, student and course info
Register_student_in_course() - adds a student to a course, if all entered values are valid
Search_student() - searches for an entered student
Add_student() - adds a student to the student table
author_info() - prints the application author name
displaying_options() - prints the options
main() - checks user input and calls various functions to add to, display or search the vehicle inventory.
"""

import mysql.connector
from mysql.connector import errors

def execute_query(connection,query):
    """
    Function name: execute_query
    Developer: Joseph Keaveny
    Date: 12-10-23

    takes an input and sends the command to the mysql database

    :param connection, query:
    :return:
    """
    action = connection.cursor()
    try:
        action.execute(query)
        connection.commit()
        action.close()
        print("added sucessfully")
    except errors as Err:
        print(f"Error: '{Err}'")

def read_db(connection,query):
    """
    Function name: read_db
    Developer: Joseph Keaveny
    Date: 12-10-23

    takes an input and gets info from the mysql database

    :param connection, query:
    :return:
    """
    task = connection.cursor()
    try:
        task.execute(query)
        read = task.fetchall()
        return read
    except errors as Err:
        print(f"Error: '{Err}'")

def Display_all_students(connection):
    """
    Function name: Display_all_students
    Developer: Joseph Keaveny
    Date: 12-10-23

    This function connects to the mysql database and returns the students in the student table
    :param connection:
    :return:
    """
    display = "SELECT * FROM student;"
    results = read_db(connection, display)
    if results:
        author_info()
        print('-' * 125)
        print("%70s" % ("Student Record:"))
        print('-' * 125)
        print("%30s%30s%30s%30s\n" % ("Student ID", "Student Fist Name", "Student Last Name", "Student Email"))
        for result in results:
            display_value = "%30s%30s%30s%30s" % (
                result[0], result[1], result[2], result[3])
            print(display_value)
    else:
        print("NO students added so far")

def Display_all_courses(connection):
    """
        Function name: Display_all_courses
        Developer: Joseph Keaveny
        Date: 12-10-23

        This function connects to the mysql database and returns the courses in the course table
        :param connection:
        :return:
        """
    display = "SELECT * FROM course;"
    results = read_db(connection, display)
    if results:
        author_info()
        print('-' * 125)
        print("%70s" % ("Courses:"))
        print('-' * 125)
        print("%30s%30s%30s\n" % ("course ID", "course title", "course credit"))
        for result in results:
            display_value = "%30s%30s%30s" % (
                result[0], result[1], result[2])
            print(display_value)
    else:
        print("No courses added yet")

def Display_all_registrations_students_and_courses(connection):
    """
        Function name: Display_all_registrations_students_and_courses
        Developer: Joseph Keaveny
        Date: 12-10-23

        This function connects to the mysql database and returns a joined table, made up of the student
        registration and course table
        :param connection:
        :return:
        """
    display = """SELECT last_name, first_name, s.student_id,c.course_id, course_title, enrollment_semester
                 FROM student s
	                JOIN registration r ON r.student_id= s.student_id
                    JOIN course c ON c.course_id = r.course_id;"""
    results = read_db(connection, display)
    if results:
        author_info()
        print('-' * 125)
        print("%70s" % ("Registration:"))
        print('-' * 125)
        print("%20s%20s%20s%20s%25s%25s\n"
              % ("Last Name", "First Name", "Student ID", "Course Code","Course Title","Semester Enrolled"))
        for result in results:
            display_value = "%20s%20s%20s%20s%25s%25s" % (
                result[0], result[1], result[2], result[3], result[4], result[5])
            print(display_value)
    else:
        print("Nothing added yet")

def Register_student_in_course(connection):
    """
            Function name: Register_student_in_course
            Developer: Joseph Keaveny
            Date: 12-10-23

            This function connects to the mysql database and adds a student to a course
            :param connection:
            :return:
            """
    print("register students in course")
    student_id = str(input("enter student ID: "))
    while True:
        if student_id[0].upper() == "N" and student_id[1] == "0" and len(student_id) == 6:
            break
        else:
            student_id = input("Enter valid student ID :")
            continue
    course_id = str(input("enter course ID: "))

    task1 = connection.cursor()
    task1.execute(f"SELECT * FROM student WHERE student_id = '{student_id}'")
    student = task1.fetchone()

    task2 = connection.cursor()
    task2.execute(f"SELECT * FROM course WHERE course_id = '{course_id}'")
    course = task2.fetchone()
    if student is None:
        print(f"No student with student ID {student_id} exists .. .. ")
    elif course is None:
        print(f"No course with course ID {course_id} exists .. .. ")
    else:
        enrollment_semester = str(input("enter enrollment semester: "))
        register = f"""
                                            INSERT INTO python_lab6.registration (student_id,course_id,enrollment_semester) 
                                            VALUES ('{student_id}','{course_id}','{enrollment_semester}')
                                            """
        execute_query(connection, register)
        print("successfully registered")

def Search_student(connection):
    """
        Function name: Search_student
        Developer: Joseph Keaveny
        Date: 12-10-23

        This function connects to the mysql database and searches for an existing student
        :param connection:
        :return:
    """
    search_student_id = input("Enter the student id to be searched:\t")
    task = connection.cursor()
    task.execute(f"SELECT * FROM student WHERE student_id = '{search_student_id}';")
    student = task.fetchone()

    if student:
        author_info()
        print('-' * 125)
        print("%70s" % ("Student Record:"))
        print('-' * 125)
        print("%30s%30s%30s%30s\n" % ("Student ID", "Student Fist Name", "Student Last Name", "Student Email"))
        display_value = "%30s%30s%30s%30s" % (student[0], student[1], student[2], student[3])
        print(display_value)
    else:
        print(f"Student with student ID {search_student_id} not found .. ..")

def Add_student(connection):
    """
    Function name: Add_student
    Developer: Joseph Keaveny
    Date: 12-10-23

    This function connects to the mysql database and adds a new student
    :param connection:
    :return:
    """
    print("adding student")
    student_id = input("enter student ID: ")
    while True:
        if student_id[0].upper()=="N" and student_id[1]=="0" and len(student_id)==6:
            break
        else:
            student_id=input("Enter valid student ID :")
            continue
    task = connection.cursor()
    task.execute(f"SELECT * FROM student WHERE student_id = '{student_id}'")
    student = task.fetchone()
    if student:
        print(f"Student with student ID {student_id} exists .. .. ")
    else:
        student_fname = str(input("enter student first name: "))
        student_lname = str(input("enter student last name: "))
        student_email = str(input("enter student email: "))
        query = f"""
                            INSERT INTO python_lab6.student (student_id,first_name,last_name,email) 
                            VALUES ('{student_id}','{student_fname}','{student_lname}','{student_email}')
                            """
        print("Student added successfully! .. ..")
        execute_query(connection,query)

def author_info():
    """
       Function name: author_info
       Developer: Joseph Keaveny
       Date: 10-10-23

       This function does not receive any argument.
       Function prints the author information.

       :return: None
       """
    author = "%120s\n%120s\n" % ("Joseph Keaveny", "StudentID: N01551957")
    #print("#*" * 60)
    print(author)

def display_options():
    """
       Function name: display_options
       Developer: Joseph Keaveny
       Date: 10-10-23

       This function does not receive any argument.
       This function only displays the options.
       Function does not return any value

       :return: None
       """
    display = """
                1) Display all students
                2) Display all courses
                3) Display all registrations -students and courses
                4) Register student in course
                5) Search student
                6) Add student 
                7) End Application
                """
    print(display)

def main():
    """
       Function name: main
       Developer: Joseph Keaveny
       Date: 12-10-23


       This function does not receive any argument.
       This function displays the options by calling the display_options functions
       It then checks if what the user entered matches with the options given, otherwise asks the user to enter again.
       If user chooses 1, display_all_students() function will be called
       If user chooses 2, display_all_courses() function will be called
       If user chooses 3, Display_all_registrations_students_and_courses() function will be called
       If user chooses 4, Register_student_in_course() function will be called
       If user chooses 5, Search_student() function will be called
       If user chooses 6, Add_student() function will be called
       If user chooses 7, the application will end.

       :return: None
       """
    user_password = 'root'
    user_name = 'root'
    host_name = 'localhost'
    db = 'python_lab6'
    plugin = 'mysql_native_password'
    connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db,
            auth_plugin=plugin)
    while True:
        display_options()
        data = input("Enter your choice .. .. ..")
        if data == '1':
            Display_all_students(connection)
        elif data == '2':
            Display_all_courses(connection)
        elif data == '3':
            Display_all_registrations_students_and_courses(connection)
        elif data == '4':
            Register_student_in_course(connection)
        elif data == '5':
            Search_student(connection)
        elif data == '6':
            Add_student(connection)
        elif data == '7':
            print("Application ending now .. .. .. ..")
            break
        else:
            print("please enter valid choice .. .. ..")
            continue

if __name__ == '__main__':
    main()
