#!/usr/bin/env python3

import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def hilbert(data):
    analytical_signal = signal.hilbert(data)
    amplitude_envelope = np.abs(analytical_signal)
    return amplitude_envelope


sample_rate, data = wav.read('test_11025hz.wav')
print(sample_rate)


# resample = 4
# data = data[::resample]
# sample_rate = sample_rate // resample

data_am = hilbert(data)

# plt.figure(figsize=(12,4))
# plt.plot(data_am)
# plt.xlabel("Samples")
# plt.ylabel("Amplitude")
# plt.title("Signal")
# plt.show()
print(data_am)
print(f"Data shape: {data_am.shape}")
frame_width = int(0.5 * sample_rate)
width, height = frame_width, data_am.shape[0] // frame_width
image = Image.new('RGB', (width, height))
px, py = 0, 0
for p in range(data_am.shape[0]):
    lum = int((data_am[p] // 40) - 60)
    if lum < 0: lum = 0
    if lum > 255: lum = 255
    image.putpixel((px, py), (lum, lum, lum))
    px += 1
    if px >= width:
        if (py % 50) == 0:
            print(f"Line saved {py} of {height}")
        px = 0
        py += 1
        if py >= height:
            break


image = image.resize((width, 4 * height))
plt.imshow(image)
plt.show()