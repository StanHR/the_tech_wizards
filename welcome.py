import win32com.client as wincl
import speech_recognition as sr
import time
speak = wincl.Dispatch("SAPI.SpVoice")



r = sr.Recognizer()
r.pause_threshold = 0.8


print("*****Student's Personal Assisstant*****")
name = 'Friend'

'''
speak.Speak("Hey {}, What's your name ?".format(name))
with sr.Microphone() as source:
    print("Speak Now !!!")
    audio = r.listen(source)
try:
    name = r.recognize_google(audio)
    print("I think you said : " + name)
except sr.UnknownValueError:
    print("I could not understand audio")



speak.Speak("Hey {}, I'm very happy to finally meet you. Kindly provide some details about you, so I can help you in"
            "your daily activities".format(name))
speak.Speak("When is your Birthday, {}".format(name))
with sr.Microphone() as source:
    print("Speak Now !!!")
    audio = r.listen(source)
try:
    dob = r.recognize_google(audio)
    print("I think you said : " + dob)
except sr.UnknownValueError:
    print("I could not understand audio")




speak.Speak("Where do you stay ?")
with sr.Microphone() as source:
    print("Speak Now !!!")
    audio = r.listen(source)
try:
    res_add = r.recognize_google(audio)
    print("I think you said : " + res_add)
except sr.UnknownValueError:
    print("I could not understand audio")


speak.Speak("When do you prefer to study ? Early morning or late night ?")
with sr.Microphone() as source:
    print("Speak Now !!!")
    audio = r.listen(source)
try:
    study_hrs = r.recognize_google(audio)
    print("I think you said : " + study_hrs)
except sr.UnknownValueError:
    print("I could not understand audio")



speak.Speak("What is your current relationship status ?")
with sr.Microphone() as source:
    print("Speak Now !!!")
    audio = r.listen(source)
try:
    rel_status = r.recognize_google(audio)
    print("I think you said : " + rel_status)
except sr.UnknownValueError:
    print("I could not understand audio")



speak.Speak("What is your current stream of education ?")
with sr.Microphone() as source:
    print("Speak Now !!!")
    audio = r.listen(source)
try:
    edu_stream = r.recognize_google(audio)
    print("I think you said : " + edu_stream)
except sr.UnknownValueError:
    print("I could not understand audio")




speak.Speak("What is your discipline in {} ?".format(edu_stream))
with sr.Microphone() as source:
    print("Speak Now !!!")
    audio = r.listen(source)
try:
    stream_disc = r.recognize_google(audio)
    print("I think you said : " + stream_disc)
except sr.UnknownValueError:
    print("I could not understand audio")
  '''


speak.Speak("What do you wish to do next ?")
print("1: Performance Analyser\n2: Attendance Manager\n3: View Upcoming Events\n4: Trip Planner\n"
            "5: Study Assistant\n" )
time.sleep(3)
with sr.Microphone() as source:
    print("Speak Now !!!")
    audio = r.listen(source)
try:
    menu_option = r.recognize_google(audio)
    print("I think you said : " + menu_option)
except sr.UnknownValueError:
    print("I could not understand audio")

if menu_option in "performance analyser":
    speak.Speak("Starting Performance Analyser")
    #call_performance_analyzer_part here

if menu_option in "attendance manager":
    speak.Speak("Starting Attendance Manager")
    #call_attenance_manager

if menu_option in "view upcoming events":
    speak.Speak("Showing Upcoming events")

if menu_option in "trip planner":
    speak.Speak("Starting Trip Planner")

if menu_option in "study assistant":
    speak.Speak("Starting the Assistant")












'''


commands = ["Hey {}, What's your name ?",
            "Hey {}, I'm very happy to finally meet you. Kindly provide some details about you, so I can help you in your daily activities. Are you ready ?",
            "When is your Birthday, {}",
            "Where do you stay {} ?",
            "When do you prefer to study {}? Early morning or late night ?",
            "What is your current stream of education,{}",
            "What is your current relationship status,{} ?"

            ]


pers_det = []

for cmd in commands:
    speak.Speak(cmd.format(name))
    with sr.Microphone() as source:
        print("Speak Now !!!")
        audio = r.listen(source)
    try:
        aud_op  = r.recognize_google(audio)
        print("I think you said : " + audio_op)
    except sr.UnknownValueError:
        print("I could not understand audio")
        pers_det.extend(audio_op)

print(pers_det)



'''















