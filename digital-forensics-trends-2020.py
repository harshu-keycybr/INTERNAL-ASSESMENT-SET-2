#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# 
# 

# In[14]:


import numpy as np
import matplotlib.pyplot as plt


labels = ['2016', '2017', '2018', '2019', '2020']
ransomware_means = [60, 85,45, 55,70]


width = 0.45       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, ransomware_means, width,  label='RANSOMWARE')

ax.set_ylabel('PERCENTAGE')
ax.set_title('DIGITAL FORENSICS TRENDS 2020')
ax.legend()

plt.show()


# In[ ]:




