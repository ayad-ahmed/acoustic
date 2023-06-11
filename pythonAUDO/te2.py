from scipy.io import wavfile

import scipy.io
import matplotlib.pyplot


samplerate, data = wavfile.read("test.wav")

length = data.shape[0] / samplerate


a,b,c,d = matplotlib.pyplot.specgram(data , scale ='dB')






#find when sound is loudest
max = 1
for i in range(0,len(data)) :
    if data[i] > data[max] :
        max = i
        

