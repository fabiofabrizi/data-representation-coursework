# Import library to connect to mysql and db config file
import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
  host = cfg.mysql['host'],
  user = cfg.mysql['user'],
  password = cfg.mysql['password']
)

cursor = db.cursor()
# Because the project is on inspirational quotes
cursor.execute("create DATABASE Quotes")

# Close the connection to the database
db.close()
cursor.close()