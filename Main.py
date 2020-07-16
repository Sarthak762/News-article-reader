import requests
import pyttsx3
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=f668c1bd470846dd9b21c7759154cacb')
response = requests.get(url)
content = response.json()
engine = pyttsx3.init()
engine.setProperty('rate',125)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
for s in content['articles']:
    engine.say(s['title'])
    engine.runAndWait()








