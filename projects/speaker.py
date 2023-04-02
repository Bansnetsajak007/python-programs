# import os

# print("Welcome to robo speaker")

# x= input("What do you want to say: ")
# command = f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{x}")'

# os.system(command)

import subprocess

print("Welcome to robo speaker")

while True:
    x = input("What do you want to say: ")
    if x == 'q':
        break
    command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'

    subprocess.call(command, shell=True)
