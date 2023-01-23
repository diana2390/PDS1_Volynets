import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user= 'root',
    password= 'Password#',
    database= 'my_first_db'
)
mycursor = mydb.cursor()
mycursor.execute('ALTER TABLE student MODIFY student_id INT AUTO_INCREMENT PRIMARY KEY')