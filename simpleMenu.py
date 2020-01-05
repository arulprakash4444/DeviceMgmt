import addDevice, addUser, removeDevice, removeUser
import json
import pprint
import clear
import time


def simplMenu():
    while(True):
        
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
        print("7.Go back")

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
            clear.clear()
            break
            

        else:
            clear.clear()
            print("i ain't heared no choice like that!")
            time.sleep(2)
            clear.clear()

if __name__ == "__main__":
    simplMenu()