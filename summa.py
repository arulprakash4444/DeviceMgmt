



# IOSARRAY = [['iphone6', 'some_number', 'some_number', '11', 'inlocker', 'None', 'None'], ['iphone6s', 'some_number', 'some_number', '10.3.2', 'inlocker', 'None', 'None'], ['iphone6splus', 'some_number', 'some_number', '13.1', 'inlocker', 'None', 'None'], ['iphonese', 'some_number', 'some_number', '13.1.3', 'inlocker', 'None', 'None'], ['iphone7', 'some_number', 'some_number', '13', 'inlocker', 'None', 'None'], ['iphone7plus', 'some_number', 'some_number', '12.4', 'inlocker', 'None', 'None'], ['iphone8', 'some_number', 'some_number', '11.3', 'inlocker', 'None', 'None'], ['iphone8plus', 'some_number', 'some_number', '12.3.1', 'inlocker', 'None', 'None'], ['iphonex', 'None', 'None', '12', 'inlocker', 'None', 'None'], ['iphonexsmax', 'None', 'None', '13.1', 'inlocker', 'None', 'None'], ['iphonexr', 'None', 'None', '12.4.1', 'inlocker', 'None', 'None'], ['ipadpro10.5', 'None', 'None', '13', 'inlocker', 'None', 'None'], ['ipadpro12.9', 'None', 'None', '13.1.3', 'inlocker', 'None', 'None'], ['ipadmini4', 'None', 'None', '10', 'inlocker', 'None', 'None'], ['ipadpro12.9_#2', 'None', 'None', '11', 'inlocker', 'None', 'None'], ['ioscablewhite_#1', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['ioscablewhite_#2', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['ioscablewhite_#3', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['ioscablewhite_#4', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['ioscablewhite_#5', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['ioscablewhite_#6', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['ioscablewhite_#7', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['ioscablewhite_#8', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['ioscablewhite_#9', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['ioscablegold_#1', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['ioscablegold_#2', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['adapter_#1', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['adapter_#2', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['adapter_#3', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['adapter_#4', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['adapter_#5', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['adapter_#6', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['adapter_#7', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['adapter_#8', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['earphone', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['applepencil', 'None', 'None', 'None', 'inlocker', 'None', 'None'], ['keyboard', 'None', 'None', 'None', 'inlocker', 'None', 'None']]
# index = 0
# IOSREFORDER = ['iphone6', 'iphone6s', 'iphone6splus', 'iphone7', 'iphone7plus', 'iphone8', 'iphone8plus', 'iphonese', 'iphonex', 'iphonexr', 'iphonexsmax', 'ipadmini4', 'ipadpro10.5', 'ipadpro12.9', 'ipadpro12.9_#2', 'ioscablegold_#1', 'ioscablegold_#2', 'ioscablewhite_#1', 'ioscablewhite_#2', 'ioscablewhite_#3', 'ioscablewhite_#4', 'ioscablewhite_#5', 'ioscablewhite_#6', 'ioscablewhite_#7', 'ioscablewhite_#8', 'ioscablewhite_#9', 'adapter_#1', 'adapter_#2', 'adapter_#3', 'adapter_#4', 'adapter_#5', 'adapter_#6', 'adapter_#7', 'adapter_#8', 'applepencil', 'earphone', 'keyboard']

# sorted_array =[]

# for i in IOSREFORDER:

#         for j in IOSARRAY:

#             if i in j[index]:

#                 sorted_array.append(j)
#                 IOSARRAY.remove(j)


# for i in sorted_array:
#     print(i)

print("._______MAIN MENU_______.")
print("|                       |")

# 


import json
# simpleSearch("Devices", "iphonese", "name", returnUser flag)
def simpleSearch(fileName, searchString, fieldName, multiple = 0):

    with open(fileName+".json", "r") as f:
        data = json.load(f)

        result = []

        flag = 0
        for item in data[fileName]:
            if item[fieldName] == searchString:
                flag = 1
                result.append(item)
                
                if multiple == 1:
                    return result

                else:
                    return result[0]


        if flag == 0:
            print("sorry not available.")
            return -1
    



