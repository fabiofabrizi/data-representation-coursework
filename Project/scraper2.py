# This implementation used to get rid of 'lxml' error when scraping a HTML page

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import os
import mysql.connector
from sqlalchemy import create_engine 


page = 1
quotes = []
authors = []
# The pages on the site only go up to 10
while page != 11:
    url = f"http://quotes.toscrape.com/page/{page}"
    response = requests.get(url)
    html = response.content
    soup = bs(html, "lxml")
    for i in soup.find_all("div",{"class":"quote"}):
        quotes.append((i.find("span",{"class":"text"})).text)
    
    for j in soup.findAll("div",{"class":"quote"}):
        authors.append((j.find("small",{"class":"author"})).text)
    
    page = page + 1
#print(quotes)
#print(authors)


# Import into a pandas dataframe:
quotesdf = pd.DataFrame(
    {'Quote':quotes,
    'Author':authors
    })

#print(quotesdf)

# Get current Dir so converted files are put in right dir
currentDir = os.path.dirname(os.path.realpath(__file__))
# Convert to CSV
quotesdf.to_csv(f'{currentDir}/quotes.csv')
# Convert to JSON
quotesdf.to_json(f'{currentDir}/quotes.json')
# Convert to Dict 
dict = quotesdf.to_dict()

#print(dict)
# Save in Current Working Dir

#
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database="quotes"
)
#
# Credentials to database connection
hostname="localhost"
dbname="quotes"
uname="root"
pwd="root"

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table                                   
quotesdf.to_sql('dailyquotes', engine, index=True, if_exists='replace', index_label="id")


# read
cursor = db.cursor()
sql = "SELECT * FROM dailyquotes"
cursor.execute(sql)
result = cursor.fetchall()
print("This is the output")
for i in result:
    print(i)
