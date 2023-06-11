import pydub
import numpy as np
import librosa
from scipy.signal import chirp, find_peaks, peak_widths

# Load audio file using pydub
audio_file = pydub.AudioSegment.from_file("white.wav")

# Convert audio to mono and extract data
audio_data = np.array(audio_file.set_channels(1).get_array_of_samples())

# Generate an impulse response using a logarithmic sweep
fs = audio_file.frame_rate
t = np.linspace(0, len(audio_data) / fs, len(audio_data), endpoint=False)
impulse_response = chirp(t, f0=20, f1=20000, t1=t[-1], method='logarithmic')

# Convolve impulse response with audio signal
convolved_signal = np.convolve(audio_data, impulse_response)

# Find peaks in the convolved signal
peaks, _ = find_peaks(convolved_signal)

# Calculate peak widths and select the widest peak
widths, _, _, _ = peak_widths(convolved_signal, peaks)
widest_peak = peaks[np.argmax(widths)]

# Calculate the decay rate and RT60 value using librosa
decay_rate = -60 / (widest_peak / fs)
rt60 = librosa.core.samples_to_time(np.argmax(convolved_signal[widest_peak:]) + widest_peak, sr=fs)

print("RT60 value:", rt60, "seconds")
