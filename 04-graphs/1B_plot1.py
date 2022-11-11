#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# df = pd.DataFrame({'count': {0: 3372, 1: 68855, 2: 17948, 3: 708, 4: 9117}}).reset_index()

# In[4]:


df


# In[7]:


plt.bar(range(len(df)), df["count"], color=plt.cm.Paired(np.arange(len(df))))
plt.show()

