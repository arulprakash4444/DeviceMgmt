
import json
import clear
import time
import searchNmatch

# ===================
# ADDING A NEW DEVICE
# ===================

def printTitle():
    print("===================")
    print("ADDING A NEW DEVICE")
    print("===================")


DeviceAttributes = ["Device_Type", "Device_Name", "Table", "OS_Version", "Asset_ID", "Serial_Num"]
Device_Types = ["Phone", "Tablet", "Cable", "Adapter", "Accessories"]
Tables = ["ios", "android"]

Attr2Array = {"Device_Type":Device_Types,"Table":Tables}

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
        if DeviceAttribute in ["Device_Type", "Table"]:
            Device[DeviceAttribute] = typeselect(Attr2Array[DeviceAttribute], "\nEnter a "+DeviceAttribute, "Enter "+DeviceAttribute+" number")

        else:
            if DeviceAttribute == "Device_Name":
                DeviceName = input("\nEnter the "+DeviceAttribute+":")
                result = searchNmatch.simpleSearch("Devices", DeviceName, DeviceAttribute)
                if result != -1:
                    return -1
                    
                else:
                    Device[DeviceAttribute] = DeviceName
            else:
                Device[DeviceAttribute] = input("\nEnter the "+DeviceAttribute+":")
                if Device[DeviceAttribute] == "":
                    Device[DeviceAttribute] = "--"
        
        clear.clear()
        printTitle()
        print("Previous input is:" + Device[DeviceAttribute])

    return Device


def printDevice(Device):
    print("")
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
    clear.clear()
    printTitle()
    theDevice = makeDevice()
    clear.clear()
    
    
    if theDevice != -1:

        printTitle()
        printDevice(theDevice)
        while(True):
            choice = input("Are you sure you want to write to the file?(y/n):")
            if slc(choice) == "y" or slc(choice) == "yes":
                writeDevice(theDevice)
                searchNmatch.inLocker(theDevice)
                clear.clear()
                print("Adding the device to the file...")
                time.sleep(2)
                clear.clear()
                break

            elif slc(choice) == "n" or slc(choice) == "no":
                clear.clear()
                print("Exiting Write to Devices.json...")
                time.sleep(2)
                clear.clear()
                break

            else:
                pass

    else:
        print("A device with a same name is already taken!")
        print('Try adding "_#(number)" to the end.')
        time.sleep(4)
        clear.clear()


if __name__ == "__main__":
    addDevice()

# pending features:
# 1.entering phone name should be slc()'ed.
# 1.5.print device in a table form.
# 2.for devices like adapters no os-version will be there so pressing enter with  empty field creates None.
# 3.changing DeviceAttributes and cascading changes.
# 4.if devices are empty proper message to go out
# 5.while giving attributes like serial number giving enter without giving anything will take that as none.

