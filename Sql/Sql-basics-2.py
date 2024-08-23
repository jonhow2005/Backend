import sqlite3
 
# generate connection
connection = sqlite3.connect("gfg.db")
 
crsr = connection.cursor()
 
#Create table
sql_command = """CREATE TABLE tablename ( 
idnumber INTEGER PRIMARY KEY, 
twentycharmaxstring VARCHAR(20), 
thirtycharmaxstring VARCHAR(30), 
onecharstring CHAR(1), 
thedate DATE);"""
sql_destroy = """ DELETE FROM tablename WHERE thedate = 2001-09-11"""
# execute statement
crsr.execute(sql_command)
 
connection.close()
