import json
import openpyxl
import array2pt
import jsonDeviceSorter
import array2xl
import time
import clear



def slc(string):
    string = string.replace(" ", "")
    string = string.lower()
    return string


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
def prepare(item, attribs):
    ordered_array = []
    for attrib in attribs:
        ordered_array.append(item[attrib])

    # print(ordered_array)
    return ordered_array


# for Item in data["Table-ios"]:
#     deldictkv(Item)


# if dict has table == ios/android send item to prepare() and put in respective array
def separate(item, iosArray, androidArray, attribs):
    if item["Table"] == "ios":
        array = prepare(item, attribs)
        iosArray.append(array)

    elif item["Table"] == "android":
        array = prepare(item, attribs)
        androidArray.append(array)


# to add "No" as 0th element[0th element] and numbers thereafter
def addNo(array):

    array[0].insert(0, "No")

    for i in range(1, len(array)):
        array[i].insert(0, i)


    # for i, item in enumerate(array,start=0):
    #     if i == 0:
    #         array[i].insert(0, "No")

    #     else:
    #         array[i].insert(0, i)


def json2arraymaker(file, attribs):
    iosArray = []

    androidArray = []

    # opening the file
    filename = file
    with open(filename, "r") as f:
        data = json.load(f)

    

    for Item in data["testarray"]:
        separate(Item, iosArray, androidArray, attribs)


    return [iosArray, androidArray]


    



# if __name__ == "__main__":
#     json2array("testarray.json")


def Json2Array(file):

    # columns to display in dat order
    attribs = ["Device_Name","Asset_ID", "Serial_Num", "OS_Version", "Alias", "Name", "Team"]

    # to identify the Device_Name index
    Device_Name_index = attribs.index("Device_Name")


    Array = json2arraymaker(file, attribs)
    
    iosArray = Array[0]
    androidArray = Array[1]

    iosArray_sorted = jsonDeviceSorter.arrayDepSort(iosArray, Device_Name_index, "ios")
    androidArray_sorted = jsonDeviceSorter.arrayDepSort(androidArray, Device_Name_index, "android")

    # inserting attribs as first element
    iosArray_sorted.insert(0, attribs)
    androidArray_sorted.insert(0, attribs[:]) 

    # the reason why this attrib has [:] is because same attrib list is referenced two times one for ios and for android while adding 
    # to top of each array , till now its fine , when the problem starts is modifying this attribs , in our case inserting "No" to 0 position
    # that is addNo() function, first when it ran for ios it adds No and same attribs is referenced while calling the function for android
    # now the attribs is already having No in it and we will insert another No to it this change is reflected in ios too becoz both are referencing 
    # same list attribs, it looks like :: ['No', 'No', 'Device_Name', 'Asset_ID', 'Serial_Num', 'OS_Version', 'Alias', 'Name', 'Team']

    
    addNo(iosArray_sorted)
    addNo(androidArray_sorted)

    print(" ")
    print("iOS Table")
    array2pt.TheArray2PT(iosArray_sorted)
    print(" ")
    print("============")
    print(" ")
    print("Android Table")
    array2pt.TheArray2PT(androidArray_sorted)

    while(True):

        choice = input("Wanna convert this into excel ?(y/n):")
        if slc(choice) == "y" or slc(choice) == "yes":
            print("\n", end="")
            array2xl.array2excel(iosArray_sorted, "ios")
            array2xl.array2excel(androidArray_sorted, "android")
            print("\n", end="")
            input("press Enter to goto MAIN MENU...")
            clear.clear()
            break

        elif slc(choice) == "n" or slc(choice) == "no":
            input("press Enter to goto MAIN MENU...")
            clear.clear()
            break

        else:
            pass

    


if __name__ == "__main__":
    Json2Array("testarray.json")


# process
# 1. getting the dic(item) from the json array.
# 2. deleting the cloumns from the array.
# 3. passing that deleted column dict(item) to rearrange it will remove the keys and pass the reordered array to table printing
