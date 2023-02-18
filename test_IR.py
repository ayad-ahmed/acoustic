"""
An example of how to use :class:`acoustics.octave.Octave`.
"""

import acoustics
from acoustics import room
import numpy as np
from acoustics.bands import octave, third



from acoustics.room import (mean_alpha, nrc, t60_sabine, t60_eyring, t60_millington, t60_fitzroy, t60_arau, t60_impulse,
                            c50_from_file, c80_from_file)



arr = acoustics.bands.octave(50, 5000)

#def main():
a = t60_impulse("untitled.wav", bands=arr, rt='t30')

#b = c50_from_file("untitled.wav", bands=arr)















#if __name__ == '__main__':
#   main()
print(a)
