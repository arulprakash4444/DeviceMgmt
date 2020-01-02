import array2pt

order = ["iphone6", "iphone7", "applepencil", "earphone", "keyboard"]

array = [["keyboard", "arul"], 
        ["earphone", "amul"],
        ["applepencil", "pranac"],
        ["iphone7", "sajara"],
        ["iphone6", "chered"]]


indexofinner = 0

sortedArray = []

for i in order:

    for j in array:

        if i in j[indexofinner]:

            sortedArray.append(j)


sortedArray.insert(0, ["Device_Name", "user"])

print(sortedArray)

def addNo(array):
    array[0].insert(0, "No")

    for i in range(1, len(array)):
        array[i].insert(0, i)

addNo(sortedArray)
print(sortedArray)


array2pt.TheArray2PT(sortedArray)