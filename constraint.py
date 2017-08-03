
# coding: utf-8

# In[1]:

import numpy as np
from math import pi, sin
from cmath import exp
#import matlab.engine

def Constraint(array, speed, freq, angle, N):
    d = np.arange(-(N - 1) / 2, (N - 1) / 2 + 1, 1) * 0.5
    dzit = 2 * pi * freq * d * sin(angle[0] * pi / 180) / speed
    #eng = matlab.engine.connect_matlab()
    #d = np.array((eng.getElementPosition(array))[1])
    #eng.quit()
    constraint = np.array([exp(complex(0, a)) for a in dzit])
    return constraint

