
# coding: utf-8

# In[1]:

import numpy as np
from lcmvweights import Lcmvweights
from constraint import Constraint

class MVDRBeamformer:
    
    def __init__(self, array, speed, freq, angle):
        self.array = array
        self.c = speed
        self.fc = freq
        self.angle = angle
        
    def step(self, rx):
        constraint = Constraint(self.array, self.c, self.fc, self.angle)
        w = Lcmvweights(rx, constraint)
        y = np.dot(rx, np.conjugate(w))
        y = y.reshape(len(y), 1)
        return [y, w]
    
    def __call__(self, rx):
        [y, w] = self.step(rx)
        return [y, w]