import addDevice, addUser, removeDevice, removeUser
import json
import pprint


def simplMenu():
    while(True):
        print("\n\n")
        print("=================")
        print("=> SIMPLE MENU <=")
        print("=================")
        print("\n")
        print("1.print devices")
        print("2.print users")
        print("3.add devices")
        print("4.add users")
        print("5.remove devices")
        print("6.remove users")
        print("7.exit")

        choice = int(input("enter ur choice:"))

        if int(choice) == 1:
            removeDevice.viewDevices()

        elif choice == 2:
            removeUser.viewUsers()

        elif choice == 3:
            addDevice.addDevice()

        elif choice == 4:
            addUser.addUser()

        elif choice == 5:
            removeDevice.removeDevice()

        elif choice == 6:
            removeUser.removeUser()

        elif choice == 7:
            print("bye!")
            break

        else:
            print("i ain't heared no choice like that!")

if __name__ == "__main__":
    simplMenu()