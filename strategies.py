from menu import *

strategy_menu_tuple = (
    "Enter new startegy",
    "Edit strategy",
    "Back to Main Menu")

strategy_menu = Menu("Strategy Menu", strategy_menu_tuple)

class Strategies:

    def strategies(self):
        while (True):
            user_selection = strategy_menu.get_option()
            match user_selection:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    break



