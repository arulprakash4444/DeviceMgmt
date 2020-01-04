import json


# ===================
# ADDING A NEW PERSON
# ===================

UserAttributes = ["Alias", "Name", "Team"]
Teams = ["officelens", "wxp","kaizala", "visio"]

Attr2Array = {"Team":Teams}

def slc(string):
    string = string.replace(" ", "")
    string = string.lower()
    return string


def typeselect(array, header, footer):
    print(header+":")
    for (index,element) in enumerate(array):
        print(str(index+1)+"."+element)

    inputValue = int(input(footer+":"))
    return array[inputValue - 1]



def makeUser():
    User = {}
    
    for UserAttribute in UserAttributes:
        if UserAttribute in ["Team"]:
            User[UserAttribute] = typeselect(Attr2Array[UserAttribute], "\nEnter a "+UserAttribute, "Enter "+UserAttribute+" number")

        else:
            User[UserAttribute] = input("\nEnter the "+UserAttribute+":")
            if User[UserAttribute] == "":
                User[UserAttribute] = "None"

    return User


def printUser(User):
    for attrib in UserAttributes:
        print(attrib+" : "+User[attrib])


def writeUser(User):
    print("Opening Users.json in read mode...")
    with open("Users.json") as f:
        print("Loading the data...")
        data = json.load(f)

    print("Appending the User...")
    data["Users"].append(User)

    print("Opening Users.json in write mode...")
    with open("Users.json", "w") as f:
        print("Dumping the data...")
        json.dump(data, f, indent=2)
        print("Write Finished!")


def addUser():
    theDevice = makeUser()
    printUser(theDevice)
    
    while(True):
        choice = input("Are you sure you want to write to the file?(y/n):")
        if slc(choice) == "y" or slc(choice) == "yes":
            writeUser(theDevice)
            break

        elif slc(choice) == "n" or slc(choice) == "no":
            print("Exiting Write to Devices.json...")
            break

        else:
            pass

if __name__ == "__main__":
    addUser()