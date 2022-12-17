# Import library to connect to mysql and db config file
import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
  host = cfg.mysql['host'],
  user = cfg.mysql['user'],
  password = cfg.mysql['password'],
  database = cfg.mysql['database']
)

cursor = db.cursor()
sql="CREATE TABLE dailyquotes (id INT AUTO_INCREMENT PRIMARY KEY, Quotes VARCHAR(450), Author VARCHAR(250))"

cursor.execute(sql)

db.close()
cursor.close()