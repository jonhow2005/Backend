import sqlite3 
  
# Connecting to sqlite 
# connection object 
connection_obj = sqlite3.connect('imgeekin.db') 

# cursor object 
cursor_obj = connection_obj.cursor() 
  
# to select all column we will use 
statement = '''SELECT * FROM GEEKER'''
  
cursor_obj.execute(statement) 
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
  
connection_obj.commit() 
  
# Close the connection 
connection_obj.close()
