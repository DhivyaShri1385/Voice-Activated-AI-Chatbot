import speech_recognition as sr
import pyttsx3
import datetime
import wikipediaapi
import webbrowser
import os
import ctypes
import requests
import smtplib
import pyjokes
import time
import dateparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your AI assistant. How can I help you?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print("Error:", e)
        speak("Sorry, I didn't catch that. Please say it again.")
        return "None"

def search_wikipedia(query):
    wiki = wikipediaapi.Wikipedia(user_agent='ChatBot/1.0 (your_email@example.com)', language='en')
    page = wiki.page(query)
    if page.exists():
        summary = page.summary[0:300]
        speak("According to Wikipedia:")
        speak(summary)
    else:
        speak("Sorry, I couldn't find anything on Wikipedia.")

def get_news():
    api_key = 'YOUR_NEWSAPI_KEY'
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}'
    response = requests.get(url)
    news = response.json()
    if news["status"] == "ok":
        speak("Here are the top news headlines:")
        for article in news["articles"][:5]:
            speak(article["title"])
    else:
        speak("Sorry, I couldn't fetch the news.")

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def send_email(to_email, subject, body):
    sender_email = "dhivyashri@gmail.com"
    sender_password = "12345"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        speak(f"Failed to send email. {e}")

def set_reminder():
    speak("What should I remind you about?")
    reminder_text = take_command()

    if reminder_text == "None":
        return

    speak("When should I remind you?")
    time_input = take_command()

    # Parse natural language time to datetime
    reminder_time = dateparser.parse(time_input)

    if not reminder_time:
        speak("Sorry, I couldn't understand the time.")
        return

    now = datetime.datetime.now()
    delay_seconds = (reminder_time - now).total_seconds()

    if delay_seconds <= 0:
        speak("The time you gave is in the past. Please try again.")
        return

    speak(f"Reminder set for {reminder_time.strftime('%I:%M %p, %B %d')}")
    
    def reminder():
        speak(f"Reminder: {reminder_text}")

    threading.Timer(delay_seconds, reminder).start()


def write_note():
    speak("What should I write?")
    note = take_command()
    if note != "None":
        with open("note.txt", "w") as f:
            f.write(note)
        speak("Note saved.")

def read_note():
    if os.path.exists("note.txt"):
        with open("note.txt", "r") as f:
            content = f.read()
        speak("Here is your note:")
        speak(content)
    else:
        speak("No note found.")

def execute_command(command):
    if 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'search' in command:
        speak("What should I search for?")
        query = take_command()
        if query and query != "None":
           speak(f"Searching for {query}")
           webbrowser.open(f"https://www.google.com/search?q={query}")

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'wikipedia' in command:
        topic = command.replace("wikipedia", "").strip()
        if topic:
           search_wikipedia(topic)
        else:
           speak("What should I search on Wikipedia?")
           topic = take_command()
           if topic and topic != "None":
               search_wikipedia(topic)
           else:
               speak("No topic provided.")

    elif 'news' in command or 'headlines' in command:
        get_news()
    elif 'joke' in command or 'funny' in command:
        tell_joke()
    elif 'what is the time' in command:
        time_str = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time_str}")
    elif 'shutdown' in command:
        speak("Shutting down system")
        os.system("shutdown /s /t 1")
    elif 'restart' in command:
        speak("Restarting system")
        os.system("shutdown /r /t 1")
    elif 'lock the system' in command:
        speak("Locking system")
        ctypes.windll.user32.LockWorkStation()
    elif 'write a note' in command or 'take a note' in command:
        write_note()
    elif 'read note' in command or 'show note' in command:
        read_note()
    elif 'send email' in command:
        speak("Who is the recipient?")
        to_email = input("Enter recipient email: ")
        speak("What is the subject?")
        subject = take_command()
        speak("What is the message?")
        body = take_command()
        #send_email(to_email, subject, body)
    elif 'remind' in command:
        set_reminder()
    elif 'exit' in command or 'stop' in command or 'quit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command()
        if command != "None":
            execute_command(command)
