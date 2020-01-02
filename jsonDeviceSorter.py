import json


device_types = ["Phone", "Tablet", "Cable", "Adapter", "Accessories"] #follow addDevices variable naming #global


def get_by_type(table, emptyarray):
    for device_type in device_types:
        Temp = []
        for item in data["Devices"]:

            if item["table"] == table:

                if item["device_type"] == device_type:
                    Temp.append(item["name"])

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

    return sorted_array
    

# if __name__ == "__main__":
#     arrayDepSort(array, index, table)
