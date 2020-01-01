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

# if devicedata != -1:
user = input("Enter the v-id:")
userdata = simpleSearch("Users", user, "vid")

TableAttributes = ["No", "Device_Name", "Device_Type", "Asset_ID", "Serial_Number", "Version", "Alias", "Name", "Team"]

def MakeEntry():
    Entry = {}

    i = 0
    Entry["No"] = i+1
    Entry["Device_Name"] = devicedata["name"]
    Entry["Device_Type"] = devicedata["device_type"]
    Entry["Asset_ID"] = devicedata["asset_id"]
    Entry["Serial_Number"] = devicedata["serial_num"]
    Entry["Version"] = devicedata["os_version"]
    Entry["Alias"] = userdata["vid"]
    Entry["Name"] = userdata["name"]
    Entry["Team"] = userdata["team"]

    return Entry

DATA = MakeEntry()
print(DATA)



# process
# after normalizing all json and python_code variables 
# get the two dictionaries from devicedata and userdata merge it if table is ios append it to ios_json_data and finally write(replace) to the file
# manage No json attrib in excelMaker
# json2table should take column_order(should be from json attribs) and row_order(custom order also) and type 

# Future
# in BIST if file(Table-ios.json and Table-android.json) is not found create ios and android json according to the ORDER of devices with user as inlocker
# if same device is used in more than one transaction while adding entry to a file should replace the existing device (i.e one file contains only one device)


