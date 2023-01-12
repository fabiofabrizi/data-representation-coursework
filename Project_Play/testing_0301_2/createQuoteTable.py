import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database="quote"
)

cursor = db.cursor()
sql="CREATE TABLE quote (id INT AUTO_INCREMENT PRIMARY KEY, quote VARCHAR(250), author VARCHAR(250))"

cursor.execute(sql)

db.close()
cursor.close()