
# coding: utf-8

# In[1]:

import random
import datetime
import numpy as np

def generater():
  lst = np.random.choice(np.arange(1, 6), 100, p = [0.5, 0.25, 0.15, 0.05, 0.05])
  return lst

print generater()


# In[ ]:



