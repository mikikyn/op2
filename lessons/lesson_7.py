import sqlite3 as sql3
# db = sql3.connect('user.db')
# cursor =  db.cursor()
# db.commit()
# db.close()


with sql3.connect('user.db') as connection:
    cursor= connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    fulname TEXT NOT NULL,
    pol INT DEFAULT 0,
    bdate DATE
    ) ''')
    # CREATE
    # cursor.execute('''INSERT INTO students (fulname, pol, bdate)
    #  VALUES ('beka',1,'2020-01-01'),('alina',2,'2020-12-31')
    #  ''')
#     read
    cursor.execute('''SELECT rowid,* FROM students''')
    print(cursor.fetchall())