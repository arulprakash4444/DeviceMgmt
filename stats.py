from prettytable import PrettyTable
import json2Array
import jsonDeviceSorter
import array2pt
import orchestrator
import clear
import time


def BringMeStats(filename):
    
    attribs = ["Device_Name", "Alias"]
    Device_Name_index = attribs.index("Device_Name")

    Array = json2Array.json2arraymaker(filename, attribs)

    TotaliOSDevices = len(Array[0])
    TotalAndroidDevices = len(Array[1])


    Array[0] = [item for item in Array[0] if item[1] != "locker"]

    Array[1] = [item for item in Array[1] if item[1] != "locker"]

    AssignediOSDevices = len(Array[0])
    AssignedAndroidDevices = len(Array[1])

    inLockeriOSDevices = TotaliOSDevices - AssignediOSDevices
    inLockerAndroidDevices = TotalAndroidDevices - AssignedAndroidDevices


    iosArray_sorted = jsonDeviceSorter.arrayDepSort(Array[0], Device_Name_index, "ios")
    androidArray_sorted = jsonDeviceSorter.arrayDepSort(Array[1], Device_Name_index, "android")

    iosArray_sorted.insert(0, attribs)
    androidArray_sorted.insert(0, attribs[:])

    json2Array.addNo(iosArray_sorted)
    json2Array.addNo(androidArray_sorted)

    print("iOS Table")
    array2pt.TheArray2PT(iosArray_sorted)
    print(" ")
    print("Total Available iOS Devices:" + str(TotaliOSDevices))
    print("Devices Assigned:" + str(AssignediOSDevices))
    print("Devices in Locker:" + str(inLockeriOSDevices))
    print(" ")
    print("============")
    print(" ")
    print("Android Table")
    array2pt.TheArray2PT(androidArray_sorted)
    print(" ")
    print("Total Available Android Devices:" + str(TotalAndroidDevices))
    print("Devices Assigned:" + str(AssignedAndroidDevices))
    print("Devices in Locker:" + str(inLockerAndroidDevices))
    print(" ")

    time.sleep(0.1)
    input("Press Enter to goto MAIN MENU...")
    clear.clear()




# if __name__ == "__main__":
#     BringMeStats("testarray.json")