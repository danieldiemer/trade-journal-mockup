from menu import Menu
from instruments import Instruments
from strategies import Strategies

print("\nWelcome to Dash. A simple trade journal and planner to aid execution.")
print("----------------------------------------------------------------------------------------------------------")

menu_tuple = (
    "Enter new trade",
    "View and edit strategies",
    "View and edit instruments",
    "Review statistics",
    "Save and exit (not functional, just quits.)")

def main():
    main_menu = Menu("Main Menu", menu_tuple)

    while (True):
       user_selection = main_menu.get_option()
       match user_selection:
           case 1:
               pass
           case 2:
               run_strategies_menu()
           case 3:
               run_instruments_menu()
           case 4:
               pass
           case 5:
               break



main()
