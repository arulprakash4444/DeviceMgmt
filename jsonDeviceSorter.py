import json


device_types = ["Phone", "Tablet", "Cable", "Adapter", "Accessories"] #follow addDevices variable naming #global


def get_by_type(table, emptyarray):
    for device_type in device_types:
        Temp = []
        for item in data["Devices"]:

            if item["Table"] == table:

                if item["Device_Type"] == device_type:
                    Temp.append(item["Device_Name"])

        emptyarray.append(Temp)


def sort_sub_array(array):
    for i in range(len(array)):
        array[i].sort()


def merge_subs(array):
    arrayE = [inner for outer in array for inner in outer]
    return arrayE


def DeviceSort():

    with open("Devices.json", "r") as f:
        global data
        data = json.load(f)

    global iosdev
    iosdev = []

    global androiddev
    androiddev = []

    get_by_type("ios", iosdev)
    get_by_type("android", androiddev)

    sort_sub_array(iosdev)
    sort_sub_array(androiddev)

    global ios_sorted
    ios_sorted = merge_subs(iosdev)
    global android_sorted
    android_sorted = merge_subs(androiddev)


def arrayDepSort(array, index, table):

    DeviceSort()
    sorted_array = []

    if table == "ios":
        referenceOrder = ios_sorted

    elif table == "android":
        referenceOrder = android_sorted

    for i in referenceOrder:

        for j in array:

            if i in j[index]:

                sorted_array.append(j)
                array.remove(j)

    return sorted_array
    

# if __name__ == "__main__":
#     arrayDepSort(array, index, table)


# DEVNAMEIND = 0
# vari = arrayDepSort(IOSARRAY, 0, 'ios')

# # for i in vari:
# #     print(i)

# IOSREFORDER = ['iphone6', 'iphone6s', 'iphone6splus', 'iphone7', 'iphone7plus', 'iphone8', 'iphone8plus', 'iphonese', 'iphonex', 'iphonexr', 'iphonexsmax', 'ipadmini4', 'ipadpro10.5', 'ipadpro12.9', 'ipadpro12.9_#2', 'ioscablegold_#1', 'ioscablegold_#2', 'ioscablewhite_#1', 'ioscablewhite_#2', 'ioscablewhite_#3', 'ioscablewhite_#4', 'ioscablewhite_#5', 'ioscablewhite_#6', 'ioscablewhite_#7', 'ioscablewhite_#8', 'ioscablewhite_#9', 'adapter_#1', 'adapter_#2', 'adapter_#3', 'adapter_#4', 'adapter_#5', 'adapter_#6', 'adapter_#7', 'adapter_#8', 'applepencil', 'earphone', 'keyboard']