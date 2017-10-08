import newsapi
import json
import requests
import urllib.request
import bs4 as bs
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

apikey= "e9ee0a55cc184d7abb5495457a625bb3"

data = requests.get("https://newsapi.org/v1/articles/?source=the-times-of-india&sortBy=top&apiKey={API_KEY}".format(API_KEY=apikey))
datadict = data.json()
#print (datadict)
for x in range(0,7):
    print("{}: \n\t {} \n\t {}\n\n".format(datadict['articles'][x]["title"],datadict['articles'][x]["description"],datadict['articles'][0]["url"]))
    speak.Speak("{}: \n\t {}".format(datadict['articles'][x]["title"], datadict['articles'][x]["description"]))
