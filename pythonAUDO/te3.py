import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np

# Load audio file
audio_file = "output.wav"
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
        
        rt30 =  ((cntr2-cntr1)*(duration))/len(db[0])
        
        rt60 = rt30 * 2
    
    
    

    
    return rt60
    
    

    
print("reverberation RT60 is : " , calculate_rt60())

