import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user= 'root',
    password= 'Password#',
    database= 'my_first_db'
)
mycursor = mydb.cursor()
# Task 2
mycursor.execute('CREATE TABLE student (student_id int, student_name varchar(255))')

# Task 3
mycursor.execute('CREATE TABLE employee (employee_id int AUTO_INCREMENT PRIMARY KEY, employee_name varchar(255), salary int(6))')