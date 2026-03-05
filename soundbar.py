#VB-Audio Virtual Cable

import keyboard
import sounddevice as sd
import soundfile as sf
import numpy as np

#1. key reckognition

def fart1():
    print("test")
    data, sample = sf.read('fart1.wav')
    sd.play(data, sample)

keyboard.add_hotkey(" ", fart1)

keyboard.wait()
