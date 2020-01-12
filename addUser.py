import json
import time
import clear
import searchNmatch


# =================
# ADDING A NEW USER
# =================
def printTitle():
    print("=================")
    print("ADDING A NEW USER")
    print("=================")


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
            if UserAttribute == "Alias":
                alias = input("\nEnter the " + UserAttribute + ":")
                result = searchNmatch.simpleSearch("Users", alias, UserAttribute)
                if result != -1:
                    return -1
                    
                else:
                    User[UserAttribute] = alias

            else:
                User[UserAttribute] = input("\nEnter the "+UserAttribute+":")
                if User[UserAttribute] == "":
                    User[UserAttribute] = "--"

        clear.clear()
        printTitle()
        print("Previous input is:" + User[UserAttribute])
    return User


def printUser(User):
    print("")
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
    clear.clear()
    printTitle()
    theUser = makeUser()
    clear.clear()
    

    if theUser != -1:

        printTitle()
        printUser(theUser)
    
        while(True):
            choice = input("Are you sure you want to write to the file?(y/n):")
            if slc(choice) == "y" or slc(choice) == "yes":
                writeUser(theUser)
                clear.clear()
                print("Adding the user to the file...")
                time.sleep(2)
                clear.clear()
                break

            elif slc(choice) == "n" or slc(choice) == "no":
                clear.clear()
                print("Exiting Write to Users.json...")
                time.sleep(2)
                clear.clear()
                break

            else:
                pass

    else:
        print("A user with a same Alias is already taken!")
        time.sleep(4)
        clear.clear()


if __name__ == "__main__":
    addUser()