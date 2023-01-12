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
cursor.execute("create DATABASE quote")

# Close the connection to the database
db.close()
cursor.close()

# INSERT INTO quote (quote, author) VALUES ("Watchoo talkin\' \'bout, Willis?", "Arnold, \'Diff\'rent Strokes\'");