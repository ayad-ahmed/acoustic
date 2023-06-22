import librosa
import numpy as np

# Step 1: Load the clean speech and noise signals
clean_speech, sr_clean = librosa.load('TTSclear.wav', sr=None)  # Replace with the path to your clean speech file
background_noise, sr_noise = librosa.load('outputSII.wav', sr=None)  # Replace with the path to your background noise file

# Step 2: Measure the characteristics of the speech signal (e.g., RMS energy)
speech_rms = np.sqrt(np.mean(clean_speech**2))

# Step 3: Measure the characteristics of the noise signal (e.g., RMS energy)
noise_rms = np.sqrt(np.mean(background_noise**2))

# Step 4: Perform spectral analysis
speech_spectrum = np.abs(librosa.stft(clean_speech))
noise_spectrum = np.abs(librosa.stft(background_noise))

# Step 5: Calculate the modulation transfer function (MTF)

noise_spectrum = np.resize(noise_spectrum, speech_spectrum.shape)

mtf = speech_spectrum / noise_spectrum

# Step 6: Calculate the Articulation Index (AI) for each frequency band
ai = np.zeros_like(mtf)
for i in range(mtf.shape[0]):
    for j in range(mtf.shape[1]):
        if mtf[i, j] > 1:
            ai[i, j] = 1 - (1 / mtf[i, j])
        else:
            ai[i, j] = mtf[i, j]

# Step 7: Calculate the SII by summing the AI values across frequency bands
sii = np.sum(ai) / ai.size

print("SII:", sii)
