# Testing the insert

# Import library to connect to mysql and db config file
import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
  host = cfg.mysql['host'],
  user = cfg.mysql['user'],
  password = cfg.mysql['password'],
  database = cfg.mysql['database']
)

# Insertion
# make cursor active, enter information, execute sql, commit to db and close connection

cursor = db.cursor()
sql="insert into dailyquotes (Quotes, Author) values (%s,%s)"
values = ("Watchoo talkin' about Willis?", "Arnold, Diff'rent Strokes")

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)


db.close()
cursor.close()