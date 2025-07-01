import webbrowser
import speech_recognition as sr
import pyttsx3
import pyaudio
import os
import pygame
import requests
from openai import OpenAI
from gtts import gTTS


recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',150)

def talkAkira(text):
    engine.say(text)
    engine.runAndWait()

def findcommand():
    pass


if __name__ == "__main__":
    talkAkira("Intializing Akira....")
    r =sr.Recognizer()

while True:
    with sr.Microphone() as command_source:
        r.adjust_for_ambient_noise(command_source,duration=5)
        talkAkira("Listening Command...")
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

        except sr.WaitTimeoutError:
            talkAkira("I didn't hear anything. Please say a command.")
        except sr.UnknownValueError:
            talkAkira("Please repeat")
        except sr.RequestError as e:
            talkAkira("Speech recognition error.")


