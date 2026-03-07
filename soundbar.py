#VB-Audio Virtual Cable

import keyboard
import sounddevice as sd
import soundfile as sf
import numpy as np
import winsound
print(sd.query_devices())

def play_sound(path):
    data, sample = sf.read(path)
    sd.play(data, sample, device=12)
    winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def stop_sound():
    sd.stop()
    winsound.PlaySound(None, winsound.SND_PURGE)

keyboard.add_hotkey('x', stop_sound)
keyboard.add_hotkey('q', play_sound, args=('fart1.wav',))
keyboard.add_hotkey('w', play_sound, args=('bethowen.wav',))

keyboard.wait()
