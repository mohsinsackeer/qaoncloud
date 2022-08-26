import mysql.connector

mydb = mysql.connector.connect(
  host="", #add the host
  user="",    #add user name
  password="", #and the password of user
  database=""    #add the name of the database
)

mycursor = mydb.cursor()

mycursor.execute(" CREATE TABLE version (lan varchar(32), charset varchar(32), name varchar(32), id varchar(32), class varchar(32), title varchar(32), role varchar(32), target varchar(32), type varchar(32), value varchar(32))")
