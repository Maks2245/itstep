import sqlite3

connection = sqlite3.connect('Dz_BD.sl3')
cur = connection.cursor()

cur.execute("CREATE TABLE Table_01 (name TEXT);")
connection.commit()


cur.execute("INSERT INTO Table_01 (name) VALUES ('Data');")
cur.execute("INSERT INTO Table_01 (name_1) VALUES ('Temperature');")
connection.commit()

cur.execute("UPDATE Table_01 SET name = 'Data - 16.01.2025' WHERE rowid = 1;")
cur.execute("UPDATE Table_01 SET name_1 = 'Temperature - 0' WHERE rowid = 2;")
connection.commit()

cur.execute("SELECT rowid, name FROM Table_01;")
connection.commit()


res = cur.fetchall()
print(res)

connection.close()