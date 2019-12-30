# before thet first we will play with quering with created json.

import json
import pprint


# for device in data["Devices"]:
#     if device["name"] == "i phone9":
#         deletedItem = data["Devices"].pop(data["Devices"].index(device))
#         print(deletedItem, end="\n")


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
            if device["name"] == searchString:
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
    viewDevices()
    deviceName = input("Enter a device name to search:")
    theDevice = simpleSearch(deviceName)
    
    while(theDevice != -1):
        choice = input("Are you sure you want to erase device from the file?(y/n):")
        if slc(choice) == "y" or slc(choice) == "yes":
            eraseDevice(theDevice)
            break

        elif slc(choice) == "n" or slc(choice) == "no":
            print("Exiting Erase from Devices.json...")
            break

        else:
            pass


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
