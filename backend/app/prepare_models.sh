curl -o recasepunc.zip https://alphacephei.com/vosk/models/vosk-recasepunc-ru-0.22.zip
unzip recasepunc.zip
mv vosk-recasepunc-ru-0.22/ recasepunc
rm -rf recasepunc.zip

cd ../model_big
curl -o ./model.zip https://alphacephei.com/vosk/models/vosk-model-ru-0.22.zip
unzip model.zip
mv vosk-model-ru-0.22/ model_big
rm -rf model.zip

cd ../model_smail
curl -o ./model.zip https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip
unzip model.zip
mv vosk-model-small-ru-0.22/ model_smail
rm -rf model.zip
