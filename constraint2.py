
# coding: utf-8

# In[ ]:



# In[1]:

import numpy as np
from math import pi, sin, cos
from cmath import exp
import matlab.engine

def Constraint(array, speed, freq, angle, N):
    eng = matlab.engine.start_matlab()
    d = np.array(eng.getElementPosition(array))
    eng.quit()
    elang = angle[1] * pi / 180
    azang = angle[0] * pi / 180
    ang = np.array([cos(elang)*cos(azang ), cos(elang)*sin(azang ), sin(elang)]).transpose()
    dzit = 2 * pi * freq * np.dot(d.transpose(),ang) / speed
    constraint = np.array([exp(complex(0, a)) for a in dzit])
    return constraint


