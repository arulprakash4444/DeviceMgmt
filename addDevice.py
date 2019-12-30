
import json


# ===================
# ADDING A NEW DEVICE
# ===================

DeviceAttributes = ["device_type", "name", "table", "os_version", "asset_id", "serial_num"]
device_types = ["Phone", "Tablet", "Cable", "Adapter", "Accessories"]
tables = ["ios", "android"]

Attr2Array = {"device_type":device_types,"table":tables}

def slc(string):
    string = string.replace(" ", "")
    string = string.lower()
    return string


def typeselect(array, header, footer):
    print(header+":")
    for (index,element) in enumerate(array):
        print(str(index+1)+"."+element)

    inputValue = int(input(footer+":"))
    return array[inputValue - 1]



def makeDevice():
    Device = {}
    
    for DeviceAttribute in DeviceAttributes:
        if DeviceAttribute in ["device_type", "table"]:
            Device[DeviceAttribute] = typeselect(Attr2Array[DeviceAttribute], "\nEnter a "+DeviceAttribute, "Enter "+DeviceAttribute+" number")

        else:
            Device[DeviceAttribute] = input("\nEnter the "+DeviceAttribute+":")
            if Device[DeviceAttribute] == "":
                Device[DeviceAttribute] = "None"

    return Device


def printDevice(Device):
    for attrib in DeviceAttributes:
        print(attrib+" : "+Device[attrib])


def writeDevice(Device):
    print("Opening Devices.json in read mode...")
    with open("Devices.json") as f:
        print("Loading the data...")
        data = json.load(f)

    print("Appending the device...")
    data["Devices"].append(Device)

    print("Opening Devices.json in write mode...")
    with open("Devices.json", "w") as f:
        print("Dumping the data...")
        json.dump(data, f, indent=2)
        print("Write Finished!")


def addDevice():
    theDevice = makeDevice()
    printDevice(theDevice)
    
    while(True):
        choice = input("Are you sure you want to write to the file?(y/n):")
        if slc(choice) == "y" or slc(choice) == "yes":
            writeDevice(theDevice)
            break

        elif slc(choice) == "n" or slc(choice) == "no":
            print("Exiting Write to Devices.json...")
            break

        else:
            pass

if __name__ == "__main__":
    addDevice()

# pending features:
# 1.entering phone name should be slc()'ed.
# 1.5.print device in a table form.
# 2.for devices like adapters no os-version will be there so pressing enter with  empty field creates None.
# 3.changing DeviceAttributes and cascading changes.
# 4.if devices are empty proper message to go out
# 5.while giving attributes like serial number giving enter without giving anything will take that as none.

