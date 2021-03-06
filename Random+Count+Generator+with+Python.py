
# coding: utf-8

# In[6]:

import random
import datetime
import numpy as np
import Queue
import threading

class Q1:
  def __init__(self):
    self.lst = []
    self.freq = {}
    self.q = Queue.Queue()
    self.output = []

  def generater(self):
    for num in np.random.choice(np.arange(1, 6), 100, p = [0.5, 0.25, 0.15, 0.05, 0.05]):
      self.q.put(num)
      self.lst.append(num)
    return self.lst

  def frequency(self):
    for num in self.lst:
      if num not in self.freq:
        self.freq[num] = 0.01
      else:
        self.freq[num] += 0.01
    return self.freq

  def writer(self):
    for _ in range(5):  
      while not self.q.empty():
        t = threading.Thread(target = self.generater, args = (self))
        t.start()
        self.output.append(str(self.q.get()) + " --> " + str(datetime.datetime.now()))
    return self.output

q1 = Q1()
print q1.generater()
print q1.frequency()
print q1.writer()


# In[ ]:



