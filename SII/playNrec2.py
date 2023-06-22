import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import threading
import paramiko
import os


def record():
    # Code for task 1
    print("Executing task 1")
    stdin, stdout, stderr = client.exec_command('python /home/pi1/Desktop/mic.py')

def play():
    # Code for task 2
    print("Executing task 2")
    stdin, stdout, stderr = client.exec_command('python testspeaker.py /home/pi1/Desktop/test.wav')




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

sftp = client.open_sftp()
remote_path = '/home/pi1/output.wav'
current_folder = os.path.dirname(os.path.abspath(__file__))
local_path = os.path.join(current_folder, 'output.wav')
sftp.get(remote_path, local_path)
sftp.close()





audio_file = local_path
y, sr = librosa.load(audio_file)

# Get the duration of the audio in seconds
duration = librosa.get_duration(y=y, sr=sr)


# Calculate spectrogram
spec = np.abs(librosa.stft(y))

# Convert power spectrogram to dB scale
db = librosa.amplitude_to_db(spec, ref=np.max)

# Plot spectrogram in dB scale
plt.figure(figsize=(12, 8))
librosa.display.specshow(db, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram in dB scale')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()


cntr1=0
cntr2=0

def calculate_rt60() :
    
    
    cntr1=0
    cntr2=0
    
    
    
    #find first instance of signal
    
    for i in db[64] :
        if i > -30   :
            print("greatest value is : " , i)
            break
        
    for j in db[64] :
    
        if i == j :
            print("at position : " ,cntr1)
            break
        cntr1 = cntr1 + 1
    
    #find the instance at which sound decays by 30db
    
    for k in db[64][cntr1:] :
        if k  <=  i -30   :
            print("end value is : " ,k)
            break
    
    
    for l in db[64] :

        if l == k :
            print("at position : " ,cntr2)
            break
        cntr2 = cntr2 + 1
    
    #calculating rt60
        
        rt30 =  ((cntr2-cntr1)*(duration))/len(db[0])-0.29
        
        rt60 = rt30 * 2
    
    
    

    
    return rt60
    
    

    
print("reverberation RT60 is : " , calculate_rt60())
