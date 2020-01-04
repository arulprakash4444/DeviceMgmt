# before thet first we will play with quering with created json.

import json
import pprint


# for device in data["Devices"]:
#     if device["name"] == "i phone9":
#         deletedItem = data["Devices"].pop(data["Devices"].index(device))
#         print(deletedItem, end="\n")


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
            if user["vid"] == searchString:
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
    viewUsers()
    userVid = input("Enter a Alias to search:")
    theUser = simpleSearch(userVid)
    
    while(theUser != -1):
        choice = input("Are you sure you want to erase user from the file?(y/n):")
        if slc(choice) == "y" or slc(choice) == "yes":
            eraseUser(theUser)
            break

        elif slc(choice) == "n" or slc(choice) == "no":
            print("Exiting Erase from Users.json...")
            break

        else:
            pass


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
