import mysql.connector
from mysql.connector import errorcode


def connect_db(db_name):
    try:
        return mysql.connector.connect(user="root", password="L0gin@ios", host='127.0.0.1', database=db_name)
    except errorcode as e:
        print(e)

def add_new_employee(name, position, course, curx):
    employee_info = (name, position)
    curx.execute('''insert into employees (name, position) values(%s, %s)''', employee_info)
    last_id = curx.lastrowid
    curx.execute('''insert into courses(emp_id, course) values(%s, %s)''', (last_id, course))
    print("executed all the queries")



connects = connect_db('hr')
curx = connects.cursor()
add_new_employee("sameer", "computer scientist", "computer science", curx)
connects.commit()
connects.close()









