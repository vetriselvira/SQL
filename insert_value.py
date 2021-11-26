import sqlite3
conn = sqlite3.connect("vetri.db")
cursor = conn.cursor()
cursor.executescript("DROP TABLE vetri1;CREATE TABLE vetri1(id,age,name);")
count = cursor.execute("select * FROM vetri1;")
#print(len(count.fetchall()))
sqlite_insert = "INSERT INTO vetri1(id,age,name)VALUES(?,?,?);"
cursor.executescript("""
    INSERT INTO vetri1 VALUES(1,32,'rajangam');
    INSERT INTO vetri1 VALUES(2,35,'kiruba');
    INSERT INTO vetri1 VALUES(3,3,'kirthi');
    INSERT INTO vetri1 VALUES(4,6,'dev');
    """)
select_all = "SELECT * FROM vetri1;"
cursor.execute(select_all)
rows = cursor.fetchall()
print("before update:")
for row in rows:
    print(row)
update_query = "ALTER TABLE vetri1 ADD COLUMN gender "
cursor.execute(update_query)
select_all = "SELECT * FROM vetri1;"
cursor.execute(select_all)
rows = cursor.fetchall()
print("after update")
for row in rows:
    print(row)
#print(len(cursor.fetchall()))
conn.commit()
conn.close()