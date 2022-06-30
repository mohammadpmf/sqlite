import sqlite3

t = sqlite3.connect(database='test.sqlite')
c = t.cursor()
q = "CREATE TABLE IF NOT EXISTS phone(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, SUBJECT TEXT NOT NULL);"
c.execute(q)
while True:
    ans = input(
"""1) insert
2) select
3) update
4) delete
q) exit
""")
    if ans == '1':
        id_ = input("id")
        name = input('name')
        subject = input('subject')
        q = "INSERT INTO phone (ID, NAME, SUBJECT) VALUES (?, ?, ?);"
        p = (id_, name, subject)
        c.execute(q, p)
        t.commit()
    elif ans=='2':
        q = "SELECT * FROM phone ORDER BY ID ASC LIMIT 2;"
        c.execute(q)
        print(c.fetchall())
    elif ans=='3':
        pass
    elif ans=='4':
        pass
    elif ans=='q':
        break
    else:
        print('Unknown command.')

t.close()
print('end')