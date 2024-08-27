# SQL
# CRUD

import sqlite3
with sqlite3.connect('game.db') as connection:
    cursor=connection.cursor()
    # cursor.execute('''DROP TABLE IF EXISTS users''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(55) NOT NULL,
    nickname TEXT NOT NULL,
    old INTEGER DEFAULT 7
    ) ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS games(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gamename TEXT NOT NULL,
    users_id INTEGER,
    FOREIGN KEY(users_id) REFERENCES users(id)  
    )''')

    # cursor.execute('''INSERT INTO users(name, nickname)
    # VALUES('beka','ECLIPSE'),('beka','ZODIAC')''')

    cursor.execute('''SELECT * FROM users WHERE id>1 ORDER BY id DESC ''')
    for row in cursor.fetchall():
        print(row)
    print()
    # cursor.execute('''INSERT INTO games (gamename,users_id)
    #  VALUES ('LOL',2),('LOL',2)''')

    cursor.execute('''SELECT * FROM games   ''')
    for row in cursor.fetchall():
        print(row)
    print()

    cursor.execute('''SELECT users.nickname, games.gamename
    FROM users
    JOIN games ON users.id = games.users_id
    ''')
    for row in cursor.fetchall():
        print(row)

    cursor.execute('''DELETE FROM users WHERE id =2''')
    print()
    cursor.execute('''SELECT * FROM users''')
    for row in cursor.fetchall():
        print(row)

        cursor.execute('''UPDATE users SET name ="beka" WHERE id=1 ''')

