# Welcome to service for recognition and processing audio to text 👋

This service is designed to transcribe audio to text. It takes mp3 audio as input (cuts off the first 10 seconds) and outputs text. The transcription functionality is implemented using
[VOSK](https://alphacephei.com/vosk/) speech recognition toolkit.

### Core tool stack:

* Python 3.9
* FastAPI
* VOSK
* Pydub
* Streamlit
* Requests

## 🚀 Usage

### Installation backend
```BASH
git clone https://github.com/geksogen/Scalable_Streamlit-_Apps.git
cd backend/app
mkdir save
sh prepare_models.sh
sudo apt-get update
sudo apt install python3-pip
sudo apt install ffmpeg
pip3 install -r ../requirements.txt
# run backend
python3 ./main.py
```

### Installation frontend
```BASH
git clone https://github.com/geksogen/Scalable_Streamlit-_Apps.git
cd frontend/app
pip3 install -r ../requirements.txt
pip3 install --upgrade jinja2
# run frontend
python3 -m streamlit run main.py
```
### ✨ Demo

<p align="center">
    <img width="500" align="center" src="https://github.com/geksogen/Scalable_Streamlit-_Apps/raw/master/spech_to_text/index.png?raw=true" alt="demo"/>
</p>

### 🤝 Contributing

Contributions, issues and feature requests are welcome.<br />
Feel free to check [issues page](https://github.com/kefranabg/readme-md-generator/issues) if you want to contribute.<br />

### Author

👤 **Geksogen**

- Github: [@geksogen](https://github.com/geksogen)
- Telegram: [@Andrey_Totshin](https://t.me/Andrey_Totshin)

### 📝 License

Copyright © 2022 [Geksogen](https://github.com/geksogen).
This project is [MIT](https://github.com/) licensed.