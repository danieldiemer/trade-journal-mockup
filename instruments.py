from menu import *

instrument_menu_tuple = (
    "Enter new instrument",
    "Edit instrument",
    "Back to Main Menu")

instrument_menu = Menu("Instrument Menu", instrument_menu_tuple)

class Instruments:
    def __init__(self, name, symbol, tick, dollars_per_tick):
        self.name = name
        self.symbol = symbol 
        self.tick = tick
        self.dollars_per_tick = dollars_per_tick

    def add_new_instrument():
        new_instrument = Instrument(name, symbol, tick, dollars_per_tick)
        print("You have added a new instrument with the following specs: ")
        print("Name: " + new_instrument.name)
        print("Symbol: " + new_instrument.symbol)
        print("Tick Value: " + new_instrument.tick)
        print("$ per tick: " + new_instrument.dollars_per_tick)

    def instruments(self):
        while (True):
            user_selection = instrument_menu.get_option()
            match user_selection:
                case 1:
                    add_new_instrument()
                case 2:
                    pass
                case 3:
                    break




