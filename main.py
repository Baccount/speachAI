# convert users voice to text
import speech_recognition as sr
from getResponse import askAI
import subprocess

# create recognizer and mic instances
r = sr.Recognizer()
mic = sr.Microphone()
while True:
    # get microphone input
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    # transcribe speech to text
    text = r.recognize_google(audio)
    # print the transcribed text
    print(f"You said: {text}")


    # upload the text to open ai and get the response
    response = askAI(question=text)

    # speak the response
    print(response)
    
    subprocess.run(["say", response])
