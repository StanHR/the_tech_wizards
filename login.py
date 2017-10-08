import pymysql
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")



class Login():
    def login_check(self):
        speak.Speak("Enter Your Username :")
        username = input()
        speak.Speak("Enter Your Password :")
        password = input()
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', db='hackathon')
        except:
            speak.Speak("Could not connect to the Database. Try again later !")
            return -1
        if conn != "":
            conn = conn.cursor()
            login_query = 'select * from users_auth where username = "'+username+'" and password = "'+password+'"'
            login_res = conn.execute(login_query)
            if login_res == 0:
                speak.Speak("Invalid Username or Password. Try again !")
                return 0
            else:
                name_query = 'select name from stud_pers_info where username = "'+username+'"'
                name = conn.execute(name_query)
                if name == 0:
                    name = "Friend"
                    speak.Speak("Hello Friend.")
                    return [name, username]
                else:
                    name = conn.fetchone()
                    speak.Speak("Welcome back {}.".format(name[0]))
                    return name[0]
        return
