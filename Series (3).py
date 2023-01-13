#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Write a Python program to add, subtract, multiple and divide two Pandas Series.
import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Add two series:")
print(ds)
ds = ds1 - ds2
print("Subtract two series:")
print(ds)
ds = ds1 * ds2
print("Multiply two series:")
print(ds)
ds = ds1 / ds2
print("Divide two series:")
print(ds)


# In[ ]:




