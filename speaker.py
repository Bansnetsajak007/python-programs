import pyttsx3

with open('sample.txt', 'r') as file:
    file_content=file.readlines()

engine=pyttsx3.init()

for i in file_content:
    engine.say(i)
    engine.runAndWait()