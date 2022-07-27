import mysql.connector

mydb = mysql.connector.connect(
  host="", #enter the host name
  user="", #enter the user name
  password="", #enter the password of the user
  database=""  #enter the name of the database
)

mycursor = mydb.cursor()

sql = "DROP TABLE version" #enter the table name

mycursor.execute(sql)