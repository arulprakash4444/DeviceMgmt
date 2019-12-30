import json
import pprint

def simpleSearch(fileName, searchString, fieldName):
    foundFlag = 0

    with open(fileName+".json", "r") as f:
        data = json.load(f)
        for item in data[fileName]:
            if item[fieldName] == searchString:
                print(item, end="\n") 
                foundFlag = 1
                return item
        
        if foundFlag == 0:
            print("Item not found!")
            return -1

# simpleSearch("Devices", "iphonese", "name")



device = input("enter the device:")
devicedata = simpleSearch("Devices", device, "name")

if devicedata != -1:
    user = input("Enter the v-id:")
    userdata = simpleSearch("Users", user, "vid")

TableAttributes = ["No", "Device_Name", "Device_Type", "Asset_ID", "Serial_Number", "Version", "Alias", "Name", "Team"]

def MakeEntry():
    Entry = {}

    i = 0
    for TableAttribute in TableAttributes:
        Entry[TableAttribute] = i+1
