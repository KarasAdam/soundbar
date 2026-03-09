# Configuration: Replace with your Virtual Cable ID (check console output on startup)
#CABLE_OUTPUT_ID = 12

import keyboard
import sounddevice as sd
import soundfile as sf
import numpy as np
import winsound


def get_best_cable_id():
    """Scans available audio devices and selects CABLE Input using the DirectSound API."""
    devices = sd.query_devices()

    for index, dev in enumerate(devices):
        dirver_name = sd.query_hostapis(dev['hostapi'])['name']
        if 'CABLE Input' in dev['name'] and 'DirectSound' in dirver_name:
            return index

    for index, dev in enumerate(devices):
        if 'CABLE Input' in dev['name']:
            return index

CABLE_OUTPUT_ID = get_best_cable_id()
print(f"Successfully connected to Virtual Cable (DirectSound) on port: {CABLE_OUTPUT_ID}")

def play_sound(path, volume=1.0):
    """
        Reads a WAV file and plays it simultaneously to the
        Virtual Cable (for Discord) and your default system output (for you).
        """
    data, sample = sf.read(path)
    data = data*volume
    # Play to Virtual Cable
    sd.play(data, sample, device=CABLE_OUTPUT_ID)
    # Play to local headphones (Windows only)
    winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def stop_sound():
    """Immediately stops all audio playback on both devices."""
    sd.stop()
    winsound.PlaySound(None, winsound.SND_PURGE)

# Hotkeys Setup
keyboard.add_hotkey('-', stop_sound)
keyboard.add_hotkey('1', play_sound, args=('your_sound2.wav',1.0))
keyboard.add_hotkey('f', play_sound, args=('your_sound2.wav',2.0))
keyboard.add_hotkey('r', play_sound, args=('your_sound2.wav',1.0))

# Keep the script running
keyboard.wait()
