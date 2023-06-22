import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import threading
import paramiko
import os
import time


def record():
    # Code for task 1
    print("Executing task 1")
    stdin, stdout, stderr = client.exec_command('python /home/pi1/Desktop/micSII.py')

def play():
    # Code for task 2
    print("Executing task 2")
    stdin, stdout, stderr = client.exec_command('python testspeaker.py /home/pi1/Desktop/TTSclear.wav')




# SSH connection details for the remote PC
hostname = 'pi1'
port = 22
username = 'pi1'
password = 'raspberry'

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote PC
client.connect(hostname, port, username, password)




# Create thread objects
thread1 = threading.Thread(target=play)
thread2 = threading.Thread(target=record)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Main program continues after the threads have finished
print("All threads have finished")



# fetch the output file
time.sleep(5)

sftp = client.open_sftp()
remote_path = '/home/pi1/outputSII.wav'
current_folder = os.path.dirname(os.path.abspath(__file__))
local_path = os.path.join(current_folder, 'outputSII.wav')
sftp.get(remote_path, local_path)
sftp.close()

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




print("done")
