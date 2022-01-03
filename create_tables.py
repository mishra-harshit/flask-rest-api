import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

# query = '''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'''
query = "DROP TABLE items;"
cur.execute(query)
query = '''CREATE TABLE IF NOT EXISTS items (name text, price real)'''
cur.execute(query)
cur.execute("Insert into items values ('test',10.99)")
con.commit()
con.close()