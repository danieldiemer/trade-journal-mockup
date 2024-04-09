from menu import *
from instruments import *
from strategies import *

print("\nWelcome to Dash. A simple trade journal and planner to aid execution.")
print("----------------------------------------------------------------------------------------------------------")

main_menu_tuple = (
    "Enter new trade (not functional)",
    "View and edit strategies",
    "View and edit instruments",
    "Review statistics (not functional)",
    "Save and exit (not functional, just quits.)")

main_menu = Menu("Main Menu", main_menu_tuple)

def main():

    while (True):
       user_selection = main_menu.get_option()
       match user_selection:
           case 1:
               pass
           case 2:
               Strategies.strategies(user_selection)
           case 3:
               Instruments.instruments(user_selection)
           case 4:
               pass
           case 5:
               break


main()