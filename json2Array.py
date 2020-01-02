import json
import openpyxl
import array2pt
import jsonDeviceSorter

#standAlone

# # columns to delete
# delKeys =["No"]
#
#
# def deldictkv(item):
#     print("inside delete fn")
#     for attrib in delKeys:
#         del item[attrib]


# order or remove column according to attribs (! Duplication column not allowed b'coz of prettytable)
def prepare(item):
    ordered_array = []
    for attrib in attribs:
        ordered_array.append(item[attrib])

    # print(ordered_array)
    return ordered_array


# for Item in data["Table-ios"]:
#     deldictkv(Item)


# if dict has table == ios/android send item to prepare() and put in respective array
def separate(item):
    if item["Table"] == "ios":
        array = prepare(item)
        iosArray.append(array)

    elif item["Table"] == "android":
        array = prepare(item)
        androidArray.append(array)


# to add "No" as 0th element[0th element] and numbers thereafter
def addNo(array):
    array[0].insert(0, "No")

    for i in range(1, len(array)):
        array[i].insert(0, i)


def json2array(file):
    global iosArray
    iosArray = []

    global androidArray
    androidArray = []

    # opening the file
    filename = file
    with open(filename, "r") as f:
        data = json.load(f)

    # columns to display
    global attribs
    attribs = ["Alias", "Device_Name", "Team"]

    # to identify the Device_Name index
    Device_Name_index = attribs.index("Device_Name")

    for Item in data["relation"]:
        separate(Item)

    iosArray_sorted = jsonDeviceSorter.arrayDepSort(iosArray, Device_Name_index, "ios")
    androidArray_sorted = jsonDeviceSorter.arrayDepSort(androidArray, Device_Name_index, "android")

    # inserting attribs as first element
    iosArray_sorted.insert(0, attribs)
    androidArray_sorted.insert(0, attribs[:])

    addNo(iosArray_sorted)
    addNo(androidArray_sorted)


    print("iOS Table")
    array2pt.TheArray2PT(iosArray_sorted)
    print(" ")
    print("============")
    print(" ")
    print("Android Table")
    array2pt.TheArray2PT(androidArray_sorted)



# if __name__ == "__main__":
#     json2array("testarray.json")


# json2array("testarray.json")


# process
# 1. getting the dic(item) from the json array.
# 2. deleting the cloumns from the array.
# 3. passing that deleted column dict(item) to rearrange it will remove the keys and pass the reordered array to table printing
