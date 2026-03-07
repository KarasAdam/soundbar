#VB-Audio Virtual Cable

import keyboard
import sounddevice as sd
import soundfile as sf
import numpy as np
import winsound
print(sd.query_devices())
#1. key reckognition

def fart1():
    print(f"działa")
    data, sample = sf.read('fart1.wav')
    sd.play(data, sample, device=12)
    winsound.PlaySound('fart1.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

keyboard.add_hotkey(" ", fart1)

keyboard.wait()
