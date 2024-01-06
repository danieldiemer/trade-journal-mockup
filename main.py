from menu import Menu

print("\nWelcome to Dash. A simple trade journal and planner to help execution.")
print("----------------------------------------------------------------------------------------------------------")

menu_tuple = ("Enter new trade",
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
               pass
           case 3:
               pass
           case 4:
               pass
           case 5:
               break



main()
