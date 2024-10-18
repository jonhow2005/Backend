def connect():
    import sqlite3
    #connect to sql
    connection = sqlite3.connect("filenameOrdirectory.db")

    crsr = connection.cursor()
 
    # error check
    print("Connected")

def createtable():
    #Create table
    sql_command = """CREATE TABLE tablename ( 
    idnumber INTEGER PRIMARY KEY, 
    twentycharmaxstring VARCHAR(20), 
    thirtycharmaxstring VARCHAR(30), 
    onecharstring CHAR(1), 
    thedate DATE);"""

def delete():
    sql_delete = """DELETE FROM tablename WHERE thedate = 2001-09-11"""
    sql_full_remove = """DELETE FROM tablename"""
    # execute statement
    crsr.execute(sql_command)

def insert():
   # insert data
  sql_command = """INSERT INTO tbl VALUES (0, "?",\
  "value2", " ", "2000-01-01");"""
  crsr.execute(sql_command(input("GimedatId")))
  #mm 2 alter data to be inserted and insert again
  sql_command = """INSERT INTO tbl VALUES (1, "value1 2nd", "value2 2nd",\
  "", "1980-10-28");"""
  crsr.execute(sql_command)

def select(): 
    sqlibidilect ="""SELECT FROM table COUNT(DISTINCT savesta) WHERE kumalala=  'hey quandale dingle here'"""
    #COUNT AVG SUM MIN MAX                    ^optional                      IN (OPTION1,  OPTION2, OPTION3)
    select2 = """SELECT FROM table WHERE column = 'arbitrary value' LIMIT 10 """
    select3  = """SELECT FROM table WHERE column = 'arbitrary value' LIKE '%skibiditoilet%'"""
    # '^[bopyes]__ba[m-f]{}%' is a string that starts with: Any letter besides B, O, P, Y, E or S, followed by two letters of any kind, followed by 'ba' and any letter within the range of m-f proceeded by an escaped character.
def update(): 
    sqlipdate = """UPDATE table SET value = 'new value' WHERE column = 'arbitrary value'""""
    
def fetch():
    crsr.execute(statement) 
    Selection = Str(input("All/Custom Amount/One"))  
    print(Selection, "data set(s)") 
    if Selection == All:
        output = cursor_obj.fetchall()
    elif Selection == "one":
        output = cursor_obj.fetchmany(Selection) 
    else:
        output = cursor_obj.fetchone() 
    for row in output: 
        print(row)


def close():
  connection.close()

