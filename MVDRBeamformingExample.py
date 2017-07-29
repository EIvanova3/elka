
# coding: utf-8

# In[1]:

import matlab.engine
#eng = matlab.engine.start_matlab()
eng = matlab.engine.connect_matlab()


# In[2]:

import numpy as np
import scipy.io as sio


# In[3]:

from beamformer import MVDRBeamformer


# In[4]:

#input data
LightSpeed = 299792458
freq = 300e6
incidentAngle = [45, 0]
array = eng.phased.ULA('NumElements', 5., 'ElementSpacing', 0.5);
eng.quit()
rx = sio.loadmat('signals.mat')
rx = np.array(rx.get('rx', None))


# In[5]:

#  [y, w] = beamformer(x) and [y, w] = beamformer.step(x) are equivalent
beamformer = MVDRBeamformer(array, LightSpeed, freq, incidentAngle)
[y_my, w_my] = beamformer.step(rx)


# In[6]:

y = sio.loadmat('result.mat')
y = np.array(y.get('y', None))
np.testing.assert_almost_equal(y_my, y)


# In[7]:

print(w_my)


# In[ ]:



