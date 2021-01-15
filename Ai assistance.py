import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')               #our pc have two inbuilt voices (male(DAvid) & female(Zira)
# print(voices[1])                                    #gives the voices id/location and details about voice
engine.setProperty('voice',voices[1].id)            #HEre we are using Zara's Voice if youhave to change it to male just make change "voices[0].id"


def speak(audio):
    '''
    Used To speak
    :param audio:
    :return:
    '''
    engine.say(audio)
    engine.runAndWait()             #All the "say()" texts won’t be said unless the interpreter encounters "runAndWait()"
                                    #That's Why we use it



def wishME():
    '''
    Wish user according to time. Time depends on system
    :return:
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("gOOD Afternoon sIR")
    else:
        speak("good Evening")

    speak("I am A.K. Please tell me How may i help you")


def takefunc():
    '''
    It takes microphone input from the user and returns string output
    :return:
    '''



def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
            print(f"User said: {query}\n")  # User query will be printed.

        except Exception as e:
            # print(e)
            print("Say that again please...")  # Say that again will be printed in case of improper voice
            return "None"  # None string will be returned
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishME()
    while (True):
        query = takeCommand().lower()

        #logic for task based on query

        if 'wikipedia' in query:
            try:
                speak('Searchng wikipedia...')
                query = query.replace('wikipedia', "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
            except Exception as e:
                speak("couldn't recognize your voice please Say again ")
                pass

        elif 'Open google' in query:
            webbrowser.open("www.google.com",new=2)

        elif 'Open Youtube' in query:
            webbrowser.open("www.youtube.com",new=2)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\Gana\\july20\\songs\\hindi'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\vinud\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Vinayak' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vinud03@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'stop jarvis' in query or 'jarvis stop' in query:
            break