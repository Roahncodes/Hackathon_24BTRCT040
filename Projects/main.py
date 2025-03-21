import speech_recognition as sr
import webbrowser
import pyttsx3


engine = pyttsx3.init()
#Listen for the wake word "Jarvis"



def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
     if("open google" == c.lower):
          webbrowser.open("https://google.com")
     elif("open facebook" == c.lower):
          webbrowser.open("https://facebook.com")
     elif("open instagram" == c.lower):
          webbrowser.open("https://instagram.com")
     elif("open linkedin" == c.lower):
          webbrowser.open("https://linkedin.com")
     elif("open spotify" == c.lower):
          webbrowser.open("https://spotify.com")


          
     
#Get word from microphone
if __name__== "__main__":
    speak("Helloo, Initializing Jarvis")
    while True: 
        #recognizing audio from mic
        r = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:       
                print("Listening...")   
                audio = r.listen(source, timeout=5, phrase_time_limit = 5 )  
            command = r.recognize_google(audio)    
            if command.lower() == "Jarvis" :
                speak("YEAH!!, IM LISTENING")
                #Listen for command
                with sr.Microphone() as source:       
                    print("YEH JARVIS ACTIVE")   
                    audio = r.listen(source, timeout=5, phrase_time_limit = 5 )  
                command = r.recognize_google(audio)    

                processCommand(command)
        except Exception as e:
                print("Error, {0}".format(e)) 
