import uvicorn
from fastapi import File
from fastapi import FastAPI
import aiofiles
from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment
import subprocess
import json
import os
import config

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome from the API backend"}

@app.post("/{style}")
async def post_endpoint(style: str, file: bytes = File(...)):

    #Save Upload file to disk s
    async with aiofiles.open('./save/soung.mp3', 'wb') as out_file:
        await out_file.write(file)  # async write

        startMin = 0
        startSec = 0
        endMin = 0
        endSec = 60

        # Time to miliseconds
        startTime = startMin * 60 * 1000 + startSec * 1000
        endTime = endMin * 60 * 10000 + endSec * 10000

        # Opening file and extracting segment
        song = AudioSegment.from_mp3('./save/soung.mp3')
        extract = song[startTime:endTime]

        ## Saving extract
        extract.export('./save/extract.mp3', format="mp3")

        # NLP processing
        SetLogLevel(0)
        x = config.STYLES[style]
        if not os.path.exists(x):
            print(
                "Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
            exit(1)

        # Set Frame Rate
        FRAME_RATE = 16000
        CHANNELS = 1

        model = Model(str(x))
        rec = KaldiRecognizer(model, FRAME_RATE)
        rec.SetWords(True)

        # pydub preprocessing audio file
        mp3 = AudioSegment.from_mp3("./save/extract.mp3")
        mp3 = mp3.set_channels(CHANNELS)
        mp3 = mp3.set_frame_rate(FRAME_RATE)

        rec.AcceptWaveform(mp3.raw_data)
        result = rec.Result()
        text = json.loads(result)["text"]

        #cased = subprocess.check_output('python3 ./recasepunc/recasepunc.py predict recasepunc/checkpoint', shell=True,
        #                               text=True, input=text)

    return {"name": text}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081)
