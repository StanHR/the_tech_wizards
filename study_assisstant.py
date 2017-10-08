import urllib.request
#from google import search
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")
import speech_recognition as sr


class StudyAssistant():

    def search(self,url,name):
        import menu
        try:
            links = []
            for url in search('{}'.format(url), tld='com.pk', lang='es', num=3, start=0, stop=1):
                links.append(url)
            print(links)
            i = 1
            for link in links:
                user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
                url = link
                headers = {'User-Agent': user_agent, }
                request = urllib.request.Request(url, None, headers)  # The assembled request
                response = urllib.request.urlopen(request)
                data = response.read()  # The data u need
                mat = data.decode()
                f = open("study_helpers{}.html".format(i), "w", encoding="utf-8")
                f.write(mat)
                i = i + 1
            speak.Speak("Data Collection is done !!!")
            print("\n\n\n")
        except NameError:
            print("There was some errror in downloading the study materials.")
        m = menu.Menu()
        speak.Speak("You're being redirected back to the Main menu")
        m.menu_options(name)



    def text_search(self,name):
        print("Enter the search keyword")
        keyword = input()
        print("Do you have any preferred website for this keyword ?")
        website = input()
        url = keyword + ' ' + website
        print("Search Keyword : {}".format(url))
        s = StudyAssistant()
        s.search(url,name)


    def voice_search(self, name):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 0.8
            speak.Speak("Enter the Search Keyword")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Keyword : " + text)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again !")
        keyword = text.split('Google Speech Recognition thinks you said', 1)

        with sr.Microphone() as source:
            r.pause_threshold = 0.8
            speak.Speak("Enter your preferrend website")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Website : " + text)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again !")
        website = text.split('Google Speech Recognition thinks you said', 1)

        url = keyword +' '+website
        s = StudyAssistant()
        s.search(url,name)


    def search_method(self,name):
        print("1: Search by Text\n2: Search by Speech Recognition")
        method = input()
        if method == '1':
            ts = StudyAssistant()
            ts.text_search(name)
        if method == '2':
            vs = StudyAssistant()
            vs.voice_search(name)




