# Configuration: Replace with your Virtual Cable ID (check console output on startup)
CABLE_OUTPUT_ID = 12

import keyboard
import sounddevice as sd
import soundfile as sf
import numpy as np
import winsound

print("Available Audio Devices:")
print(sd.query_devices())
print("\nSoundboard is running. Press 'X' to stop any sound.")

def play_sound(path):
    """
        Reads a WAV file and plays it simultaneously to the
        Virtual Cable (for Discord) and your default system output (for you).
        """
    data, sample = sf.read(path)
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
keyboard.add_hotkey('q', play_sound, args=('sound1.wav',))
keyboard.add_hotkey('w', play_sound, args=('sound2.wav',))

# Keep the script running
keyboard.wait()
