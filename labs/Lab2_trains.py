# Lab workthrough from the second week

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

# Does it work?
# print(doc.toprettyxml()) # Comment out once it's confirmed it's working

with open("trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)


objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
#print("The train codes are below:\n")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    #print (traincode)


# Now print out the latitudes of the trains
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
#print("The train Latitudes are below:\n")
for objTrainPositionsNode in objTrainPositionsNodes:
    trainlatnode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    trainlat = trainlatnode.firstChild.nodeValue.strip()
    #print(trainlat)

# Solution for blank lines in the file:
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
# adding the newline= '' parameter
with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    """
    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = []
        dataList.append(traincode)
        train_writer.writerow(dataList)
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
    """
    # Q8
    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)
    
    # Q9 Only store trains whose traincodes start with a D 