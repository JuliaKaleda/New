import sqlite3

conn = sqlite3.connect("hw27.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')
conn.commit()

a = ['homework', 1, 15, 'word', 16]
for i in a:
    if type(i) is str:
        cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''', [i])
        b = len(i)
        cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', (b,))
        conn.commit()
    elif type(i) is int:
        if i%2==0:
            cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', [i])
        elif i%2!=0:
            cursor.execute('''INSERT INTO tab_1 (col_1) VALUES ('нечётное')''')
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT*FROM tab_2''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT*FROM tab_2''')
k = cursor.fetchall()
print(len(k))
if len(k) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
    conn.commit()
elif len(k) <5:
    cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id = 1''')
    conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)