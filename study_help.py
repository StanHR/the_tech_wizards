# Get the first 5 hits for "google 1.9.1 python" in Google Pakistan
from google import search
import urllib.request


import speech_recognition as sr
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()
r.pause_threshold = 1
option = 0
while option != '3' :
    print("1: Search by Text\n2: Search by Voice\n3: Exit")
    option = input()

    if option == '2':
        speak.Speak("What is the name of the topic ?")
        with sr.Microphone() as source:
            print("Speak Now !!!")
            audio = r.listen(source)
        try:
            keyword = r.recognize_google(audio)
            print("I think you said : " + keyword)
        except sr.UnknownValueError:
            print("I could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


        with sr.Microphone() as source:
            print("Speak Now !!!")
            audio = r.listen(source)
        try:
            website = r.recognize_google(audio)
            print("I think you said : " + website)
        except sr.UnknownValueError:
            print("I could not understand audio")
        query = keyword + website

    elif option == '1':
        print("What is the name of the topic ?")
        keyword = input()+" "
        print("Do you have any website preference ?")
        website = input()
        query = keyword + website
        print(query)

    elif option == '3':
        exit()


    else:
        print("Invalid Input")

    try:
        links = []
        for url in search('{}'.format(keyword), tld='com.pk', lang='es', num=3, stop=2):
            links.append(url)
            print(links)

        i = 1
        for link in links :
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            url = link
            headers={'User-Agent':user_agent,}
            request=urllib.request.Request(url,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data = response.read() # The data u need
            mat = data.decode()
            f = open("study_helpers{}.html".format(i), "w", encoding="utf-8")
            f.write(mat)
            i = i + 1
        print("done")

    except NameError:
        print("GoodBye")




