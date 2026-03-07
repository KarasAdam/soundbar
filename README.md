  Simple Python Discord Soundboard
A lightweight, global hotkey-controlled soundboard written in Python. It allows you to play .wav files directly into Discord, Zoom, or Games through a Virtual Audio Cable, while simultaneously monitoring the audio through your own headphones.

  Key Features
Dual Output: Audio is mirrored to both your Virtual Cable (for others to hear) and your default system output (for you to hear).

Global Hotkeys: Works while you are in-game or your browser is focused.

Smart Overlap Prevention: Playing a new sound automatically stops the current one, preventing a chaotic mess of overlapping audio.

Emergency Kill-Switch: Press a dedicated key (default is '-') to immediately silence all audio.

Low Latency: Uses sounddevice and winsound for minimal delay.

  Prerequisites
Virtual Audio Cable: You must have a virtual audio driver installed. The most popular choice is VB-CABLE Virtual Audio Cable.

Windows OS: This script uses the winsound library for local monitoring, which is native to Windows.

Python 3.10+

  Installation & Setup
Clone the repository:

git clone https://github.com/KarasAdam/soundbar.git
cd soundbar

Install dependencies:

pip install -r requirements.txt
Configure your Audio Device ID:

Run the script once: python soundbar.py.

It will print a list of all detected audio devices in your console.

Find the ID of "CABLE Input (VB-Audio Virtual Cable)".

Open soundbar.py and update the CABLE_OUTPUT_ID variable at the top:

Python
CABLE_OUTPUT_ID = 12  # Replace with your ID

  Adding Your Own Sounds
Place your .wav files into the project folder.

Map them to your preferred keys at the bottom of soundbar.py:

Python
keyboard.add_hotkey('f5', play_sound, args=('meme_sound.wav',))

  Discord Configuration
To make it work, you need to tell Discord to listen to the "other end" of the virtual pipe:

Open Discord -> User Settings -> Voice & Video.

Set Input Device to CABLE Output (VB-Audio Virtual Cable).

Keep your Output Device set to your actual headphones.

  License
This project is open-source and available under the MIT License. Feel free to use and modify it!
