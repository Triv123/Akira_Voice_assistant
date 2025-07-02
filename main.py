import webbrowser
import speech_recognition as sr
import pyttsx3
import pyaudio
import os
import pygame
import requests
from openai import OpenAI
from gtts import gTTS
from newsapi import NewsApiClient
from dotenv import load_dotenv
import musicLibrary


recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',150)
load_dotenv()

def news_headlines():
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news,cnn&pageSize=5&apiKey={NEWS_API_KEY}"


    r = requests.get(url)
    print("Status Code:", r.status_code)

    if r.status_code == 200:
        data = r.json()
        print("Full response:", data)  # <--- this will help you debug

        articles = data.get("articles", [])
        if articles:
            talkAkira("Here are the top news headlines.")
            for i, article in enumerate(articles, 1):
                talkAkira(f"Headline {i}: {article['title']}")
        else:
            talkAkira("No news articles found.")
    else:
        talkAkira("Failed to fetch the news.")


def talkAkira(text):
    engine.say(text)
    engine.runAndWait()

def findcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open x" in c.lower():
        webbrowser.open_new_tab("https://x.com")
    elif "play" in c.lower():
        song = c.lower().split("play", 1)[1].strip()
    
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            talkAkira("Song not found in music library.")
    elif "news" or "headlines" in c:
        news_headlines()
    else:
        

if __name__ == "__main__":
    talkAkira("Intializing Akira....")
    r =sr.Recognizer()


with sr.Microphone() as command_source:
    r.adjust_for_ambient_noise(command_source,duration=1)
    talkAkira("Listening Command...")
    while True:
        try:
            cmd_audio = r.listen(command_source,None,phrase_time_limit=10)
            command= r.recognize_google(cmd_audio)
            print("Heard Command: ",command)


            if "exit" in command.lower():
                talkAkira("Exiting. Bye Trivikram")
                exit()
            else:
                try:
                    findcommand(command)
                except Exception as e:
                    talkAkira("Sorry,This feature is not yet available Try another command.")

        # except sr.WaitTimeoutError:
        #     talkAkira("I didn't hear anything. Please say a command.")
        except sr.UnknownValueError:
            talkAkira("Please repeat")
        except sr.RequestError as e:
            talkAkira("Speech recognition error.")


