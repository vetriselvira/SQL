import sqlite3
conn = sqlite3.connect("vetri.db")
cursor = conn.cursor()
conn.executescript("CREATE TABLE IF NOT EXISTS 'outlet'(outlet_id INT PRIMARY KEY,outlet_name VARCHAR(100),outlet_address VARCHAR(100));")
outlet_id = input("Enter outlet_id:")
outlet_name = input("Enter outlet_name:  ")
oulet_address = input("Enter outlet address:")
sql = "insert into outlet(outlet_id,outlet_name,outlet_address) values(?,?,?)"
val = (outlet_id,outlet_name,oulet_address)
#cursor.execute("INSERT INTO outlet VALUES(1,'Main_outlet','Rt:9,Oldbridge');")
cursor.execute(sql,val)
select_all = "SELECT * FROM outlet;"
cursor.execute(select_all)
print(cursor.fetchall())
conn.commit()
conn.close()



#sql = "insert into emp(id, name, salary) values(%d, %s, %s)"

#val = (id, name, salary)