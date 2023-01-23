import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user= 'root',
    password= 'Password#',
    database= 'my_first_db'
)
mycursor = mydb.cursor()
sql = 'INSERT INTO student(student_id, student_name) VALUES (%s, %s)'
val = ("01", "John")
mycursor.execute(sql, val)
mydb.commit()

sql2 = 'INSERT INTO employee(employee_id, employee_name, salary) VALUES (%s, %s, %s)'
val2 = ("01", "John", "10000")
mycursor.execute(sql2, val2)
mydb.commit()