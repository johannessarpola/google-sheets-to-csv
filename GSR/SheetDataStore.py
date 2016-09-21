import json, os
from pprint import pprint
storePath = '.store'+os.path.sep

def getSheetIds(filename):
    with open(filename) as data_file:    
        data = json.load(data_file)
    return data

def getSheetIdsRelativeAsJson(filename):
    path = getRelPathToStore()+filename
    with open(path) as data_file:    
        data = json.load(data_file)
    return data

def getRelPathToStore():
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    return os.path.join(path, storePath)

def readData(filepath):
    data = getSheetIds(filepath)
    return data

def parseDataToSheet(data):
    # for(data.)
    sheets = []
    for de in data.items():
        name = de[0]
        subelements = de[1]
        idstr = subelements['id']
        worksheets = subelements['Sheets']
        s = Sheet(name,idstr,worksheets)
        sheets.append(s)
    return sheets

# Class to map the json to a object
class Sheet:
    def __init__(self, name, idstr, sheetslist):
        self.name = name
        self.idstr = idstr
        self.sheetslist = sheetslist

    def __str__(self):
        return str(self.name)+' '+str(self.idstr)+' '+str(self.sheetslist)
    def __repr__(self):
        return self.__str__()
