import json
import openpyxl
import array2pt

#TheArray
TheArray = []

# opening the file
with open("testarray.json", "r") as f:
    data = json.load(f)

# columns to display
attribs = ["No", "Device_Name", "Alias", "Team"]
TheArray.append(attribs)

# # tables precursor
# pt = PrettyTable()
# pt.field_names = attribs

# # columns to delete
# delKeys =["No"]
#
#
# def deldictkv(item):
#     print("inside delete fn")
#     for attrib in delKeys:
#         del item[attrib]


def prepare(item):
    ordered_array = []
    for attrib in attribs:
        ordered_array.append(item[attrib])

    # print(ordered_array)
    return ordered_array


# for Item in data["Table-ios"]:
#     deldictkv(Item)


# for Item in data["Table-ios"]:
#     print(Item)


for Item in data["Table-ios"]:
    array = prepare(Item)
    TheArray.append(array)
    # pt.add_row(array)




array2pt.TheArray2PT(TheArray)

# pt.add_row(list(Item.values()))
# variable = prepare(data["Table-ios"][1])

# for Item in data["Table-ios"]:
#     print(Item)

# print(pt)
# print(pt.field_names)
# print(pt.attributes)

# process
# 1. getting the dic(item) from the json array.
# 2. deleting the cloumns from the array.
# 3. passing that deleted column dict(item) to rearrange it will remove the keys and pass the reordered array to table printing

