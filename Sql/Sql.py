def connect:
    import sqlite3

    #connect to sql
    connection = sqlite3.connect("filenameOrdirectory.db")

    crsr = connection.cursor()
 
    # error check
    print("Connected")

def createtable:
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

def insert:
   # insert data
  sql_command = """INSERT INTO tbl VALUES (0, "?",\
  "value2", " ", "2000-01-01");"""
  crsr.execute(sql_command(input("GimedatId")))
 
#mm 2 alter data to be inserted and insert again
  sql_command = """INSERT INTO tbl VALUES (1, "value1 2nd", "value2 2nd",\
"", "1980-10-28");"""
crsr.execute(sql_command)
# close connection
connection.close()
