
# coding: utf-8

# In[1]:

import numpy as np
from math import sqrt 

def Lcmvweights(rx, constraint):
    X = rx / sqrt(len(rx))
    R = np.linalg.qr(np.conjugate(X), mode='r')
    temp = np.linalg.solve(np.dot(np.conjugate(R).transpose(), R), constraint)
    w = temp / np.dot(np.conjugate(constraint).transpose(), temp)
    return w

