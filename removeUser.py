# before thet first we will play with quering with created json.

import json
import pprint
import clear
import time
import searchNmatch


def printTitle():
    print("==============")
    print("ERASING A USER")
    print("==============")

# for device in data["Devices"]:
#     if device["name"] == "i phone9":
#         deletedItem = data["Devices"].pop(data["Devices"].index(device))
#         print(deletedItem, end="\n")

UserAttributes = ["Alias", "Name", "Team"]
def printUser(User):
    print("")
    for attrib in UserAttributes:
        print(attrib+" : "+User[attrib])


def slc(string):
    string = string.replace(" ", "")
    string = string.lower()
    return string


def viewUsers():
    print("The users:")
    with open("Users.json", "r") as f:
        data = json.load(f)

        if not data["Users"]:
            print("There are no Users added to the file.")

        else:
            for user in data["Users"]:
                print(user)


def simpleSearch(searchString):
    foundFlag = 0

    with open("Users.json", "r") as f:
        data = json.load(f)
        for user in data["Users"]:
            if user["Alias"] == searchString:
                print(user, end="\n") 
                foundFlag = 1
                return user
        
        if foundFlag == 0:
            print("User not found!")
            return -1


def eraseUser(user4Deletion):
    print("Opening Users.json in read mode...")
    with open("Users.json") as f:
        print("Loading the data...")
        data = json.load(f)

        print("Erasing the user")
        deletedItem = data["Users"].pop(data["Users"].index(user4Deletion))
        
        print("Opening Users.json in write mode...")
        with open("Users.json", "w") as f:
            print("Dumping the data...")
            json.dump(data, f, indent=2)
            print("Write Finished!")

        print("\n Deleted User(s):")
        print(deletedItem)


def removeUser():
    clear.clear()
    printTitle()

    Alias = input("Enter a Alias to search:")
    theUser = simpleSearch(Alias)
    clear.clear()
    

    if theUser != -1:

        printTitle()
        printUser(theUser)

        # result = searchNmatch.simpleSearch("testarray", Alias, "Alias", 1)
        # if result[1] != "locker":
        #     print(deviceName + " is assigned to " + result[1] + "!")
        #     print("Erasing the Device will remove the relation too!")

        while(True):
            choice = input("Are you sure you want to erase "+ Alias +" from the file?(y/n):")
            if slc(choice) == "y" or slc(choice) == "yes":
                eraseUser(theUser)
                clear.clear()
                print("Erasing the User from the file...")
                time.sleep(2)
                clear.clear()
                break

            elif slc(choice) == "n" or slc(choice) == "no":
                clear.clear()
                print("Exiting Erase from Users.json...")
                time.sleep(2)
                clear.clear()
                break

            else:
                pass

    else:
        print("User not found!")
        time.sleep(2)
        clear.clear()



if __name__ == "__main__":
    removeUser()
# devicename = input("enter device name:")
# theDevice = simpleSearch(devicename)
# print("return check:::: "+str(theDevice))

# with open("Devices.json", "r") as f:
#         data = json.load(f)
#         if theDevice in data["Devices"]:
#             print("device in list check:::: "+str(theDevice))


# future implementations:
# 1.implement fuzzy search
# 2.show multiple devices.
# 3.and delete from the list
