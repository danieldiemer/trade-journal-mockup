from menu import Menu

print("\nWelcome, this is Dash, not just a trading journal, but rather a trade planning and execution assist tool.")
print("----------------------------------------------------------------------------------------------------------")

menu_tuple = ("Enter new trade",
"View and edit strategies",
"View and edit instruments",
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
               break



main()
