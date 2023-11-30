class Menu:
    def __init__(self, name, menu_tuple):
        self.name = name
        self.menu_tuple = menu_tuple

    def get_option(self):
        while (True):
            self.print_menu()
            print("\n Input Selection Now:  ")
            user_selection = self.typecast_int(input())
            if type(user_selection)==int:
                selection_verified = self.verify_selection(user_selection)
                if selection_verified:
                    break
        return user_selection

    def print_menu(self):
            print("\n --   "+ self.name +"   --")
            for x in range(0,len(self.menu_tuple)):
                print (str(x+1) + ". "+ self.menu_tuple[x])

    def typecast_int(self,user_selection):
        try:
            user_selection = int(user_selection)
        except ValueError:
            print("\n----------->>> Use type integer only <<<-----------")
        return user_selection

    def verify_selection(self, user_selection):
        if user_selection<=(len(self.menu_tuple)+1) and user_selection>=1 :
            return True
        else:
            print("\n----------->>> Invalid number entered <<<-----------")
            return False
