import sqlite3
 
# generate connection
connection = sqlite3.connect("geekin.db")
 
crsr = connection.cursor()
 
#Create table
sql_command = """CREATE TABLE tablename ( 
idnumber INTEGER PRIMARY KEY, 
twentycharmaxstring VARCHAR(20), 
thirtycharmaxstring VARCHAR(30), 
onecharstring CHAR(1), 
thedate DATE);"""
sql_delete = """DELETE FROM tablename WHERE thedate = 2001-09-11"""
sql_full_remove = """DELETE FROM tablename"""
# execute statement
crsr.execute(sql_command)
 
connection.close()
