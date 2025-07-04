# Akira Voice Assistant 🧠🎙️

Akira is a Python-based voice assistant inspired by virtual assistants like Alexa, Siri, and Google Assistant. It can respond to voice commands, open websites, play music, read news, and even answer questions using ChatGPT.

---

## 🚀 Features

- 🎧 Voice Command Recognition (using SpeechRecognition)
- 🌐 Open websites (Google, YouTube, Facebook, LinkedIn, etc.)
- 🎵 Play favorite songs from a local or custom music library
- 📰 Read top headlines from News API
- 💬 Ask questions using OpenAI's ChatGPT API
- 📄 Text-to-speech responses using pyttsx3 or gTTS

---

## 🛠️ Technologies Used

- Python 3.x
- `speech_recognition`
- `pyttsx3` / `gTTS`
- `webbrowser`
- `requests`
- `openai`
- `newsapi-python`
- `dotenv` (for secure API keys)

---

## 🔧 Installation


git clone https://github.com/your-username/akira-voice-assistant.git
cd akira-voice-assistant
python -m venv venv
venv\Scripts\activate    # (Windows)
pip install -r requirements.txt




## 🗝️ Setup

Create a .env file in the project root:


OPENAI_API_KEY=your_openai_api_key
NEWS_API_KEY=your_newsapi_key


Add songs to your custom musicLibrary.py dictionary.

## 🗣️ How to Use

Just run:

python main.py
Speak commands like:

"Open YouTube"
"Play Shape of You"
"What is Python?"
"Read news"


## 📂 Folder Structure

Akira_Voice_assistant/
│
├── main.py
├── chatgpt.py
├── musicLibrary.py
├── .env
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt



## 🛡 License
This project is licensed under the MIT License.

## 🤝 Contributions
Pull requests are welcome! Feel free to fork and improve the project.


## 🌟 Star This Repo
If you like this project, please consider starring ⭐ it on GitHub!


---


I can help you polish it even more!

