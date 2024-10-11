import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess

# Initialize the text-to-speech engine for Ubuntu
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first available voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak('HELLO Ankit sir')
    speak('I am Jarvis')
    speak('Please tell me how may I help you')
   
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(e)
        print("Say it again, please.")
        return "None"
    return query

if __name__ == "__main__": 
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on the query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak('According to Wikipedia:')
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")
        
        # elif 'play music' in query:
        #     music_dir = '/path/to/your/music/directory'  # Change to your music directory
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     subprocess.run(["xdg-open", os.path.join(music_dir, songs[0])])
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "https://github.com/Ankitprajapati24"
            webbrowser.open(codePath)
