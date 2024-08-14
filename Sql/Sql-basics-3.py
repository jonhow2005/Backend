import sqlite3

idname = str("ninganote")
# connecting to the database
connection = sqlite3.connect("filename.db")

crsr = connection.cursor()
 
# insert data
sql_command = """INSERT INTO tbl VALUES (0, "?",\
"value2", " ", "2000-01-01");"""
crsr.execute(sql_command(idname))
 
# alter data to be inserted and insert again
sql_command = """INSERT INTO tbl VALUES (1, "value1 2nd", "value2 2nd",\
"", "1980-10-28");"""
crsr.execute(sql_command)
 
# save change to database
connection.commit()
 
# close connection
connection.close()
