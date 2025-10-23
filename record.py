import sounddevice as sd
import numpy as np
import wave

# 錄音參數
fs = 16000       # 取樣率
seconds = 5      # 錄音秒數
filename = "output.wav"

print("Recording...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()
print("Recording finished!")

# 儲存成 WAV
with wave.open(filename, 'w') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)  # int16 -> 2 bytes
    wf.setframerate(fs)
    wf.writeframes(recording.tobytes())
