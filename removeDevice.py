# before thet first we will play with quering with created json.

import json
import pprint
import time
import clear
import searchNmatch
import recordMani

# for device in data["Devices"]:
#     if device["name"] == "i phone9":
#         deletedItem = data["Devices"].pop(data["Devices"].index(device))
#         print(deletedItem, end="\n")

def printTitle():
    print("=================")
    print("ERASING A DEVICE")
    print("=================")


DeviceAttributes = ["Device_Type", "Device_Name", "Table", "OS_Version", "Asset_ID", "Serial_Num"]
def printDevice(Device):
    print("")
    for attrib in DeviceAttributes:
        print(attrib+" : "+Device[attrib])


def slc(string):
    string = string.replace(" ", "")
    string = string.lower()
    return string


def viewDevices():
    print("The devices:")
    with open("Devices.json", "r") as f:
        data = json.load(f)

        if not data["Devices"]:
            print("There are no devices added to the file.")

        else:
            for device in data["Devices"]:
                print(device)


def simpleSearch(searchString):
    foundFlag = 0

    with open("Devices.json", "r") as f:
        data = json.load(f)
        for device in data["Devices"]:
            if device["Device_Name"] == searchString:
                print(device, end="\n") 
                foundFlag = 1
                return device
        
        if foundFlag == 0:
            print("Device not found!")
            return -1


def eraseDevice(device4Deletion):
    print("Opening Devices.json in read mode...")
    with open("Devices.json") as f:
        print("Loading the data...")
        data = json.load(f)

        print("Erasing the device")
        deletedItem = data["Devices"].pop(data["Devices"].index(device4Deletion))
        
        print("Opening Devices.json in write mode...")
        with open("Devices.json", "w") as f:
            print("Dumping the data...")
            json.dump(data, f, indent=2)
            print("Write Finished!")

        print("\n Deleted Device(s):")
        print(deletedItem)


def removeDevice():
    clear.clear()
    printTitle()

    deviceName = input("Enter a device name to search:")
    theDevice = simpleSearch(deviceName)
    clear.clear()
    

    if theDevice != -1:
        printTitle()
        printDevice(theDevice)
        result = searchNmatch.simpleSearch("testarray", deviceName, "Device_Name")
        if result["Alias"] != "locker":
            print(deviceName + " is assigned to " + result["Alias"] + "!")
            print("Erasing the Device will remove the relation too!")

        while(True):

            choice = input("Are you sure you want to erase "+ deviceName +" from the file?(y/n):")
            if slc(choice) == "y" or slc(choice) == "yes":
                eraseDevice(theDevice)
                searchNmatch.eraseEntry(result)
                recordMani.delRdev("record", deviceName)
                clear.clear()
                print("Erasing the Device from the file...")
                time.sleep(2)
                clear.clear()
                break

            elif slc(choice) == "n" or slc(choice) == "no":
                clear.clear()
                print("Exiting Erase from Devices.json...")
                time.sleep(2)
                clear.clear()
                break

            else:
                pass

    
    else:
        print("Device not found")
        time.sleep(2)
        clear.clear()


if __name__ == "__main__":
    removeDevice()
# devicename = input("enter device name:")
# theDevice = simpleSearch(devicename)
# print("return check:::: "+str(theDevice))

# with open("Devices.json", "r") as f:
#         data = json.load(f)
#         if theDevice in data["Devices"]:
#             print("device in list check:::: "+str(theDevice))


# future implementations:
# 1.implement fuzzy search
# 2.show multiple devices.
# 3.and delete from the list
