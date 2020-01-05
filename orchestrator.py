# # from stats import BringMeStats
# import searchNmatch


# def typeselect(array, header, footer):
#     print("\n")
#     print(header+":")
#     for (index,element) in enumerate(array):
#         print(str(index+1)+"."+element)

#     inputValue = int(input(footer+":"))
#     return inputValue


# def Orchestrator():
#     while(True):
#         options = ["View Stats", "Device Transfer", "Preview", "Add/Remove", "Exit"]
#         choice = typeselect(options, "MAIN MENU", "Enter and option")


#         if choice == 1:
#             # BringMeStats("testarray.json")

#         elif choice == 2:
#             searchNmatch.SearchAndMatch()

#         # elif choice == 3:
#         #     searchNmatch.S2earchAndMatch()

#         elif choice == 5:
#             break



# Orchestrator()

import searchNmatch
import stats
import json2Array
import simpleMenu
import time
import clear


def MainMenu():
    while(True):

        print("=================")
        print("=>  MAIN MENU  <=")
        print("=================")
        print("\n")
        print("1.View Stats")
        print("2.Device transfer")
        print("3.Preview")
        print("4.Edit")
        print("5.Exit")

        choice = int(input("enter ur choice:"))

        if int(choice) == 1:
            clear.clear()
            stats.BringMeStats("testarray.json")

        elif choice == 2:
            clear.clear()
            searchNmatch.SearchAndMatch()

        elif choice == 3:
            clear.clear()
            json2Array.Json2Array("testarray.json")

        elif choice == 4:
            clear.clear()
            simpleMenu.simplMenu()

        elif choice == 5:
            clear.clear()
            print("bye!")
            time.sleep(2)
            break

        else:
            clear.clear()
            print("I ain't heared no choice like that!")
            time.sleep(2)
            clear.clear()
            


if __name__ == "__main__":
    MainMenu()
    
