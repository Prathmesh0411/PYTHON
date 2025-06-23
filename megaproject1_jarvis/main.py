import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary 
# import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your_news_api_key_here"  # Replace with your actual News API key

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com") 
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    # elif "news" in c.lower():
    #     r = request.get("https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
    #     if r.status_code == 200:
    #         # Parse the JSON response
    #         data = r.json()
            
    #         # Extract the articles
    #         articales = data.get('articles', [])
            
    #         # Print the headlines
    #         for articles in articles:
    #             speak(articles['title'])
        
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
            
        # recognize speech using google 
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("ya")
                # listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                    
        except Exception as e:  
            print("Error: {0}".format(e))
            
                
    