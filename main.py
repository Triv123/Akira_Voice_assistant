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

def talkAkira(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    talkAkira("Booting Akira.")
