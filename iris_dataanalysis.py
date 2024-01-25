#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
#load the datset
df_iris = sns.load_dataset('iris')
sns.pairplot(df_iris, hue="species")
plt.savefig('iris-dataset-pair-plot.png', dpi=300, bbox_inches='tight')
plt.show()


# In[ ]:




