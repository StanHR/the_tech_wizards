from login import Login
from registration import Registration
import win32com.client as wincl
from menu import Menu
speak = wincl.Dispatch("SAPI.SpVoice")

class Home:
    def activity(self):
        speak.Speak("Please Log in")
        login = Login()
        name = login.login_check()
        while name == 0:
            name = login.login_check()
        if name == -1:
            quit(-1)
        elif name[0] == "Friend":
            reg = Registration()
            result = reg.register(name[1])
            if result == -8:
                speak.Speak("Your details have been updated. Please login again.")
                quit()
        else:
            speak.Speak("Let's get started")
            menu = Menu()
            menu.menu_options(name)


instance = Home()
instance.activity()