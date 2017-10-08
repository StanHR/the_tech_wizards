import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
import pymysql


class Registration:
    def register(self, username):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', db='hackathon', autocommit= True)
        except:
            speak.Speak("Could not connect to the Database. Try again later !")
            return -1

        speak.Speak("Welcome to the Registration Panel.")
        username = username
        speak.Speak("Enter your first name:")
        first_name = input()
        speak.Speak("Enter your Date of Birth in Y-Y-Y-Y M-M D-D format:")
        dob = input()
        speak.Speak("What is your prefferable study time ? Late night or early morning ?")
        study_pref_time = input()
        speak.Speak("What is your current relationship status ?")
        rel_status = input()
        speak.Speak("In which city do you stay ?")
        city = input()
        speak.Speak("Enter the strean of your current education")
        edu_stream = input()
        speak.Speak("Enter your discipline in {}".format(edu_stream))
        stream_discipline = input()
        speak.Speak("Which Semester are you currently studying in ?")
        sem = input()
        speak.Speak("Thanks a lot for providing the details.")
        cursor = conn.cursor()
        reg_query = 'insert into stud_pers_info(username,name,dob,study_pref_time,city,rel_status,edu_stream,stream_disc,sem) values("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(username,first_name,
                                                                dob,study_pref_time,city,rel_status,edu_stream,stream_discipline,sem)
        name = cursor.execute(reg_query)
        print(name)
        return -8

