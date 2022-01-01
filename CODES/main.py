import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes

from tkinter import *
from tkinter.ttk import *
# Create object
root = Tk()
root.title('Virtual Assistant') #window title
# Adjust size
root.geometry("1570x810")

style = Style()
# Add image file
bg = PhotoImage(file="Artboard Image.png")

def openNewWindow():
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newWindow.title("About")

    # sets the geometry of Toplevel
    newWindow.geometry("800x25")

    # A Label widget to show in toplevel
    Label(newWindow, text="Developed by 'TEAM A' © Lamisa Mashiat_ID-C201249 © Sohana Tasneem_ID-C201266 © Sadia Hossain Chowdhury_ID-C201270").pack()

# Create Canvas
canvas1 = Canvas(root, width=1570,
                 height=810)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

style.configure('TButton', font=
('Josefin Sans', 20, 'bold'),
                borderwidth='4')

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground=[('active', '!disabled', 'purple')],
          background=[('active', 'purple')])

# Create Buttons
button1 = Button(root, text="Start", command=root.destroy)
button2 = Button(root, text="About", command=openNewWindow)

# Display Buttons
button1_canvas = canvas1.create_window(250, 600,height= 50, width=150,
                                       anchor="nw",
                                       window=button1)

button2_canvas = canvas1.create_window(450, 600,height= 50, width=150,
                                       anchor="nw",
                                       window=button2)

# Execute tkinter
root.mainloop()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) for female
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<5:
        speak("Hello Lamisa. You should sleep. Good night!")

    elif hour>=5 and hour<12:
        speak("Good Morning Lamisa!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Lamisa!")

    else:
        speak("Good Evening Lamisa!")


    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"the time is {strTime}")

    base = datetime.date.today()
    dayname = datetime.datetime.now().strftime("%A")
    speak(f"today is {base}")
    speak(f"{dayname}")
    #date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
    #date_list_with_dayname = [ "%s, %s" % ((base + datetime.timedelta(days=x)).strftime("%A"), base + datetime.timedelta(days=x)) for x in range(numdays)]

    speak("I am Dory. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':

    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "D:\\Virtual Voice Assistance\\music"  # add the path of your music folder
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))  # random song

        elif 'open youtube' in query:
            speak("Opening youtube..")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com/")

        elif 'open my classroom' in query:
            speak("opening google classroom")
            webbrowser.open("https://classroom.google.com/u/2/h")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code block' in query:
            idePath = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            speak("Opening Codeblocks")
            os.startfile(idePath)
            speak("It takes a little time to open codeblocks. I know how much you hate waiting but please have patience.")

        elif 'open zoom' in query:
            zoomPath = "C:\\Users\\Asus\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            speak("Opening zoom meetings")
            os.startfile(zoomPath)

        elif 'joke' in query:
            speak("Here's one..")
            the_joke = pyjokes.get_joke()
            print(the_joke)
            speak(the_joke)

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)

        elif 'codeforces' in query:
            speak("Opening codeforces..")
            webbrowser.open("https://codeforces.com/profile/Sadia_Chowdhury")

        elif 'github' in query:
            speak("Opening github..")
            webbrowser.open("https://github.com/lamisamashiat3")

        elif 'hackerrank' in query:
            speak("Opening hackerrank..")
            webbrowser.open("https://www.hackerrank.com/sadiachowdhury22")

        elif "who am i" in query:
            speak("If you talk then definitely you are a human.")

        elif "who are you" in query:
            speak("I am your virtual assistant Dory")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Lamisa?")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'reason for your' in query:
            speak("I was created as a Minor project by Team A ")

        #elif 'find location' or 'find a location' in query:
        #    speak('What is the location?')
        #    location = takeCommand()
        #    url = 'https://google.nl/maps/place/' + location + '/&amp;'
        #    webbrowser.get().open(url)

       # elif 'email to sohana' or 'email' in query:  # write here the name of the person whom you want to send the email
            #try:
            #    speak("yeah sure. What should I write in the email?")
            #    content = takeCommand()
            #    to = "sohanatasneem12@gmail.com"  # write here the address of the person whom you want to send the email
            #   sendEmail(to, content)
            #    speak("Email has been sent!")
            #except Exception as e:
            #    print(e)
            #   speak("Sorry! I couldn't send this email")

        elif 'thank you' in query or "thanks" in query:
            speak("It's my pleasure to serve. what else I can do for you?")

        elif "exit" in query:
            speak("ok !! Dory is sleeping now . Come back soon .. Bye!!")
            exit()