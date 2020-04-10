from tkinter import *
from PIL import ImageTk,Image
import speech_recognition as sr
import pyttsx3, datetime, sys, wikipedia, wolframalpha, os, smtplib, random, webbrowser, pygame, subprocess

client = wolframalpha.Client('3X4434-2GAXRXY3X9')

#folder = 'C:\\Users\\skt\\Music\\YouTube\\'

engine = pyttsx3.init()
voices = engine.getProperty('voices')

#b_music = ['Shape Of You']
#pygame.mixer.init()
#pygame.mixer.music.load('C:\Users\Jitu\Desktop\songs' + random.choice(b_music) + '.mp3')
#pygame.mixer.music.set_volume(0.05)
#pygame.mixer.music.play(-1)


def speak(audio):
    print('Dillion:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


class Widget:
    def __init__(self):
        root = Tk()
        root.title('DILLION')
        root.config(background='YELLOW')
        width = root.winfo_screenwidth()
        height = (root.winfo_screenheight()- 80)
        root.geometry('%dx%d+0+0'%(width,height))
        #root.resizable(0, 0)
        root.iconbitmap(r'image1_R2T_icon.ico')
        img = ImageTk.PhotoImage(Image.open(r'ai.jpg'))
        panel =Label(root, image= img , bg= 'black')
        panel.pack(side="top", fill='both', expand="no")

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click \'Start Listening\' to Give commands')

        userFrame = LabelFrame(root, text="USER", font=('Black ops one', 15, 'bold'),fg='black',bg='cyan2')
        userFrame.pack(fill="both", expand="yes")

        left2 = Message(userFrame, textvariable=self.userText, fg='cyan2', bg='black')
        left2.config(font=("Black Ops One",12))
        left2.pack(fill='both', expand='yes')

        compFrame = LabelFrame(root, text="DILLION",font=('Black ops one', 15, 'bold'),fg='black',bg='cyan2')
        compFrame.pack(fill="both", expand="yes")

        left1 = Message(compFrame, textvariable=self.compText, fg='cyan2', bg='black')
        left1.config(font=("Black Ops One", 12))
        left1.pack(fill='both', expand='yes')



        btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='cyan2', fg='black',
                     command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), fg='black', bg='cyan2',
                      command=root.destroy).pack(fill='x', expand='no')

        speak('Hello, I am DILLION! made using artificial intelligence... What should I do for You?')
        self.compText.set('Hello, I am Dillion! What should I do for You?')

        root.bind("<Return>", self.clicked) 
        root.mainloop()

    def clicked(self):
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'open ccleaner' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\CCleaner\CCleaner.exe')

        elif 'open google chrome' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif 'open powerpoint' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Microsoft Office\Office14\POWERPNT.EXE')

        elif 'open youtube' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif "open VLC media player" in query:
            speak("opening vlc media player")
            subprocess.call(r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe")
        elif "who are you" in query:
            self.compText.set("I am a virtual voice assistant .... my name is DILLION !....mr. SUTHAR has made me...on 22nd march 2019 at 1:35 pm")
            speak("I am a virtual voice assistant .... my name is DILLION !....mr. SUTHAR has made me...on 22nd march 2019 at 1:35 pm")
        elif 'open google' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'where is' in query:
            query = query.split(" ")
            length = len(query)
            location = ""
            for i in range (2,length):
                location = (str(location) + " " + str(query[i]))
            speak('hold on let me find where '+ location +' is')
            webbrowser.open('www.google.nl/maps/place/' + location +'/&amp')

        elif "lets play a game" in query:
            from os import system
            system('virtual_game.py')

        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('shutdown -s')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            self.compText.set(random.choice(stMsgs))
            speak(random.choice(stMsgs))

        elif "open C drive" in query:
            system.call("c:\\")


        elif 'email' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            recipient = myCommand()
            self.userText.set(recipient)
            recipient = recipient.lower()


            if 'me' in recipient:
                try:
                    self.compText.set('What should I say? ')
                    speak('What should I say? ')
                    content = myCommand()
                    self.userText.set(content)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Username')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    self.compText.set('Email sent!')
                    speak('Email sent!')

                except:
                    self.compText.set('Email sent!')
                    speak('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')



        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye Sir, have a good day.')
            speak('Bye Sir, have a good day.')

        elif 'hello' in query:
            self.compText.set('Hello Sir')
            speak('Hello Sir')


        elif 'bye' in query:
            self.compText.set('Bye ' + 'Sir' + ', have a good day.')
            speak('Bye ' + 'Sir' + ', have a good day.')

        elif 'play music' in query:
            music_folder = 'C:\\Users\\skt\\Music\\YouTube\\'
            music = ['Edison', 'bensound-actionable', 'bensound-buddy', 'Micro', 'Lucid_Dreamer']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')

        else:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    self.compText.set(results)
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    self.compText.set(results)
                    speak(results)

            except:
                speak('I don\'t know Sir! Google is smarter than me!')
                self.compText.set('I don\'t know Sir! Google is smarter than me!')
                webbrowser.open('www.google.com')


if __name__ == '__main__':
    greetMe()
    widget = Widget()
