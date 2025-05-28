import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor, conn

    try:
        conn = pymysql.connect(host='localhost', user='root', password='2006', database='employee_data')
        mycursor = conn.cursor()

        mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
        mycursor.execute('USE employee_data')

        mycursor.execute('''
            CREATE TABLE IF NOT EXISTS data (
                Id VARCHAR(20),
                Name VARCHAR(50),
                Phone VARCHAR(15),
                Role VARCHAR(50),
                Gender VARCHAR(10),
                Salary DECIMAL(10,2)
            )
        ''')

        conn.commit()

    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong: {e}')

# Insert Function with Proper Connection Handling
def insert(id, name, phone, role, gender, salary):
    try:
        conn = pymysql.connect(host='localhost', user='root', password='2006', database='employee_data')
        mycursor = conn.cursor()

        mycursor.execute('INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s)',
                         (id, name, phone, role, gender, salary))

        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Data inserted successfully!')

    except Exception as e:
        messagebox.showerror('Error', f'Insertion failed: {e}')
def id_exist(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s', (id,))
    result = mycursor.fetchone()
    return result[0] > 0

def fetch_employees():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='2006', database='employee_data')
        mycursor = conn.cursor()
        mycursor.execute('SELECT * FROM data')
        result = mycursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        messagebox.showerror('Error', f'Fetching data failed: {e}')
        return []
def update(id, name, phone, role, gender, salary):
    try:
        conn = pymysql.connect(host='localhost', user='root', password='2006', database='employee_data')
        mycursor = conn.cursor()

        mycursor.execute('''
            UPDATE data SET Name=%s, Phone=%s, Role=%s, Gender=%s, Salary=%s WHERE Id=%s
        ''', (name, phone, role, gender, salary, id))

        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Data updated successfully!')

    except Exception as e:
        messagebox.showerror('Error', f'Update failed: {e}')

def delete(id):
    mycursor.execute('DELETE FROM data WHERE id=%s',id)
    conn.commit()


def search(option,value):
    mycursor.execute(f'SELECT * FROM data WHERE {option}=%s',value)
    result=mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()

# Call function to establish connection
connect_database()
