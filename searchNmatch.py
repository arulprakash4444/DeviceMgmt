import json
import orchestrator
import time
import clear
import recordMani

def jsonarraylen(filename):

    with open(filename + ".json", "r") as f:
        data = json.load(f)

    return len(data[filename])



def slc(string):
    string = string.replace(" ", "")
    string = string.lower()
    return string


# # simpleSearch("Devices", "iphonese", "name", returnUser flag)
# def simpleSearch(fileName, searchString, fieldName, returnUser = 0):

#     with open(fileName+".json", "r") as f:
#         data = json.load(f)

#         if fieldName == "Alias":
#             Aliases = []

#             aliasFlag = 0
#             for item in data[fileName]:
#                 if item[fieldName] == searchString:
#                     aliasFlag = 1
#                     Aliases.append(item)
#                     return Aliases


#             if aliasFlag == 0:
#                 Aliases.append(-1)
#                 print("sorry not available.")
#                 return Aliases

#             # if len(Aliases) >= 1:
#             #     return Aliases

#             # elif len(Aliases) == 0:
#             #     print("item not found!")
#             #     return -1


#         else:
#             flag = 0
#             for item in data[fileName]:
#                 if item[fieldName] == searchString:
#                     flag = 1
#                     print(item, end="\n")
                    

#                     if returnUser == 1:
#                         return (item, item["Alias"])

#                     else:
#                         return item


#             if flag == 0:
#                 print("Item not found!")
#                 return -1



# =================================================================


def simpleSearch(fileName, searchString, fieldName, multiple = 0):

    with open(fileName+".json", "r") as f:
        data = json.load(f)

        result = []

        flag = 0
        for item in data[fileName]:
            if item[fieldName] == searchString:
                flag = 1
                result.append(item)

        if flag == 1:     
            if multiple == 1:
                return result

            else:
                return result[0]


        elif flag == 0:
            print("sorry not available.")
            return -1


# =================================================================


def dictMerge(dict1, dict2):
    result = {**dict1, **dict2}
    return result


def eraseEntry(Entry):
    print("Opening testarray.json in read mode...")
    with open("testarray.json") as f:
        print("Loading the data...")
        data = json.load(f)

        print("Erasing the Entry")
        deletedItem = data["testarray"].pop(data["testarray"].index(Entry))
        
        print("Opening testarray.json in write mode...")
        with open("testarray.json", "w") as f:
            print("Dumping the data...")
            json.dump(data, f, indent=2)
            print("Write Finished!")

        print("\n Deleted Entry('s):")
        print(deletedItem)


def writeEntry(Entry):
    print("Opening testarray.json in read mode...")
    with open("testarray.json") as f:
        print("Loading the data...")
        data = json.load(f)

    print("Appending the device...")
    data["testarray"].append(Entry)

    print("Opening testarray.json in write mode...")
    with open("testarray.json", "w") as f:
        print("Dumping the data...")
        json.dump(data, f, indent=2)
        print("Write Finished!")


def SearchAndMatch():
    device = input("enter the device:")
    devicedata = simpleSearch("testarray", device, "Device_Name")

    if devicedata != -1:
        print("The device is assigned to " + devicedata["Alias"], end="\n")
        user = input("Enter the Alias:")
        userdata = simpleSearch("Users", user, "Alias")

        if userdata != -1:
            
            while(True):
                choice = input("Are you sure you want to assign "+ device + " to "+ user +"?(y/n):")
                if slc(choice) == "y" or slc(choice) == "yes":
                    # print(simpleSearch("Devices", device, "Device_Name"))
                    entry = dictMerge(simpleSearch("Devices", device, "Device_Name"), userdata)
                    eraseEntry(devicedata)
                    writeEntry(entry)

                    if devicedata["Alias"] == "locker" and user != "locker":
                        recordMani.writeNote(device + "  " + devicedata["Alias"] + " --> " + user + ". locker to user trigger.")
                        recordMani.pushCin("record", device, user)
                    elif devicedata["Alias"] != "locker" and user == "locker":
                        recordMani.writeNote(device + "  " + devicedata["Alias"] + " --> " + user + ". user to locker trigger.")
                        recordMani.modCout("record", device)
                    elif devicedata["Alias"] != "locker" and user != "locker":
                        recordMani.writeNote(device + "  " + devicedata["Alias"] + " --> " + user + ". user to user trigger.")
                        recordMani.modCout("record", device)
                        recordMani.pushCin("record", device, user)

                    else:
                        pass
                    
                    clear.clear()
                    print(device + " is transferred to " + user + ".")
                    time.sleep(2)
                    clear.clear()

                    break

                elif slc(choice) == "n" or slc(choice) == "no":
                    print("Exiting Write to testarray.json...")
                    clear.clear()
                    print("Transfer of " + device + " to " + user + " is cancelled.")
                    time.sleep(2)
                    clear.clear()
                    break

                else:
                    pass


        else:
            time.sleep(2)
            clear.clear()

    else:
        time.sleep(2)
        clear.clear()


def inLocker(Device):

    Data = simpleSearch("testarray", Device["Device_Name"], "Device_Name")
    
    if Data  != -1:

        if Data["Alias"] != "locker":
            print("The device "+ Device["Device_Name"] +" is already assigned to " + Data["Alias"] +"!")

            while(True):
                choice = input("Are you sure you want to assign "+ Device["Device_Name"] + " to locker?(y/n):")
                if slc(choice) == "y" or slc(choice) == "yes":
                    eraseEntry(Data)
                    entry = dictMerge(Device, simpleSearch("Users", "locker", "Alias"))
                    writeEntry(entry)
                    print("The device "+ Device["Device_Name"] +" is assigned to locker")
                    break

                elif slc(choice) == "n" or slc(choice) == "no":
                    print("The device "+ Device["Device_Name"] +" is assigned to " + Data["alias"])
                    print("Exiting Write to testarray.json...")
                    break

                else:
                    pass

        else:
            pass

    
    else:
        entry = dictMerge(Device, simpleSearch("Users", "locker", "Alias"))
        writeEntry(entry)



def AllInLocker():

    with open("Devices.json", "r") as f:
        data = json.load(f)

    for device in data["Devices"]:
        inLocker(device)


# AllInLocker()
# print(jsonarraylen("testarray"))
# SearchAndMatch()
# print(jsonarraylen("testarray"))
aaa = simpleSearch("testarray", "v-tebo", "Alias", 1)
print(aaa)



# process
# after normalizing all json and python_code variables 
# get the two dictionaries from devicedata and userdata merge it if table is ios append it to ios_json_data and finally write(replace) to the file
# manage No json attrib in excelMaker
# json2table should take column_order(should be from json attribs) and row_order(custom order also) and type 

# Future
# in BIST if file(Table-ios.json and Table-android.json) is not found create ios and android json according to the ORDER of devices with user as inlocker
# if same device is used in more than one transaction while adding entry to a file should replace the existing device (i.e one file contains only one device)
