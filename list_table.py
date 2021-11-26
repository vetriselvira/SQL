import sqlite3
conn = sqlite3.connect("vetri.db")
cursor = conn.cursor()
conn.executescript("DROP TABLE vetri;CREATE TABLE vetri(id,age,name);")
cursor.execute("INSERT INTO vetri VALUES(1,32,'rajangam');")
select_all = "SELECT * FROM vetri;"
cursor.execute(select_all)
print(cursor.fetchall())
conn.commit()
conn.close()