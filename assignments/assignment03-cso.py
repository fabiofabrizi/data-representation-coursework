"""
    This is assignment 03:
    Write a program to retrieve the dataset exchequer account (historical series) from the CSO
    and store it into file named cso.json

    Dataset: FIQ02 - Exchequer Account (Historical Series)
    Page URL: https://data.gov.ie/dataset/monthly-exchequer-tax-receipts-1984-present/resource/0720452e-e998-4493-9643-e814cf8470e8
    
    Dataset URL: = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

    Dataset description:

    Open Data Tax Receipts- Monthly Exchequer Tax Receipts 1984 - Present in CSV format.

    The monthly Exchequer returns are published on the second working day of the subsequent month, 
    with a press conference held each quarter. These data are all historic with the exception of 
    the data from the current year and will be updated following their publication 
    in the Exchequer Statement.

    The data is broken down as follows: 
    Customs, Excise Duty, Capital Gains Tax, Capital Acquisitions Tax, 
    Stamps, Income Tax, Corporation Tax, Value Added Tax, 
    Training and Employment Levy, Local Property Tax, Unallocated Tax Receipts
"""
# Import libraries
import requests
import json

"""
Did curl -i first on command line first.
just did below to practice commands, checking
headers, encoding, etc

print(response.status_code)
#print(response.text)
#print(response.encoding)
#print(response.headers)
#print(response.json)
#print(response.headers['content-type'])
"""
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"
response = requests.get(url)
data = response.json()
print(data)

with open("cso.json", "w") as fp:
    json.dump(data, fp)


"""
Also works this way

import pandas as pd

df = pd.read_json (r'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en')
print (df)
# save dataframe to json file
df.to_json("cso1.json")
"""
