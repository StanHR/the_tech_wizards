import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
from study_assisstant import StudyAssistant
from performance_manager import Performance_Man
import time

class Menu:
    def menu_options(self, name):
        speak.Speak("This is all what I have for you")
        print("1: Performance Analyzer\n2: Attendance Manager\n3: Events Notifier\n4: Study Assistant\n5: Smart Alarm\n6: Holiday & Trip Planner\n99: Exit")
        speak.Speak("Select the desired option")
        option = input()

        if option in ['Performance Analyzer','performance analyzer','1']:
            speak.Speak("Starting performance analyzer.")
            per_ana = Performance_Man()
            per_ana.plotter(name)


        if option in ['Attendance Manager','attendance manager','2']:
            speak.Speak("Starting attendance manager.")
        if option in ['Events Notifier','events notifier','3']:
            speak.Speak("Starting events notifier.")


        if option in ['Study Assisstant','study assisstant','4']:
            speak.Speak("Starting study assisstant.")
            sa = StudyAssistant()
            sa.search_method(name)

        if option in ['Smart Alarm','smart alarm','5']:
            speak.Speak("Starting smart alarm.")


        if option in ['Holiday & Trip Planner','holiday and planner','holiday & planneer','6']:
            speak.Speak("Starting holiday & planner")
        if option == 99:
            quit()

