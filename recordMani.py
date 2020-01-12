import json
import datetime


def writeNote(message):

    with open("transaction.txt", "a") as f:
        f.write(message + "\n")


# def addRdevice():

import pprint
 
# inserting a record to index 0 for a device 
def pushCin(filename, Device_Name, Alias):
    recordData = {}
    recordData["Alias"] = Alias
    recordData["checkin"] = datetime.datetime.now().strftime("%d-%B-%Y %a - %H:%M %p")
    recordData["checkout"] = "--"

    with open(filename + ".json", "r") as f:
        data = json.load(f)

        if Device_Name in data[filename].keys():
            data[filename][Device_Name].insert(0, recordData)

        else:
            data[filename][Device_Name] = []
            data[filename][Device_Name].insert(0, recordData)

    with open(filename + ".json", "w") as f:
        json.dump(data, f, indent=2)


# pushRecord("record", "iphone14", "v-arupra")


# to write checkout time in file
def modCout(filename, Device_Name):

    with open(filename + ".json", "r")as f:
        data = json.load(f)
    
        data["record"][Device_Name][0]["checkout"] = datetime.datetime.now().strftime("%d-%B-%Y %a - %H:%M %p")

    with open(filename + ".json", "w")as f:
        json.dump(data, f, indent=2)

# ModCout("record", "iphone14")


# import datetime

# curr = datetime.datetime.now()
# curr.strftime("%d-%B-%Y %a - %H:%M %p")

# curr1 = datetime.datetime.strptime("13-January-2020 Sun - 04:53 AM", "%d-%B-%Y %a - %H:%M %p")
# curr2 = datetime.datetime.strptime("12-January-2020 Sun - 03:50 AM", "%d-%B-%Y %a - %H:%M %p")
# print(curr1)
# print(curr2)

# diff = curr1 - curr2
# print(diff)

# pushRecord("record", "iphone6", "v-arupra")
# ModCout("record", "iphone6")
# aaa = datetime.datetime.now().strftime("%d-%B-%Y %a - %H:%M %p")

#remove device when device got deleted
def delRdev(filename, Device_Name):

    with open(filename + ".json") as f:
        data = json.load(f)

        if Device_Name in data[filename].keys():
            del data[filename][Device_Name]

        else:
            print("Device donot exist in record!")

    with open(filename + ".json", "w") as f:
        json.dump(data, f, indent=2)

    

# delRdev("record", "iphone12")



#delete record when time expires
def delRecord(filename, record):

    with open(filename + ".json") as f:
        data = json.load(f)

        flag = 0
        for Device_Name in data["record"].keys():
            if record in reversed(data["record"][Device_Name]):
                data["record"][Device_Name].pop(data["record"][Device_Name].index(record))
                flag = 1

        
        if flag == 0:
            print("oombu")
        

    with open(filename + ".json", "w") as f:
        json.dump(data, f, indent=2)
    


# record = {
#           "Alias": "v-souma",
#           "checkin": "12-January-2021 Sun - 05:19 AM",
#           "checkout": "12-January-2020 Sun - 05:21 AM"
#         }

# delRecord("record", record)

def recView(filename, Device_Name):

    with open(filename + ".json") as f:
        data = json.load(f)

    for record in data[filename][Device_Name]:
        print(record["Alias"])
        print("Check-In: " + record["checkin"])
        print("Check-Out: " + record["checkout"])

        if record["checkout"] == "--":
            duration = "It's still out there."

        else:
            curr1 = datetime.datetime.strptime(record["checkout"], "%d-%B-%Y %a - %H:%M %p")
            curr2 = datetime.datetime.strptime(record["checkin"], "%d-%B-%Y %a - %H:%M %p")
            duration = curr1 - curr2

        print("Duration: " + str(duration))

        print(" ")

recView("record", "iphone6")
