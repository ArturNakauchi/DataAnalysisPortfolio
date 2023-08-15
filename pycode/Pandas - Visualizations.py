#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


df = pd.read_csv(r"C:\Users\Artur\Desktop\Python_Projects\Ice Cream Ratings.csv")
df = df.set_index('Date')
df


# In[40]:


#changing styles with matplotlib

print(plt.style.available)
plt.style.use('dark_background')


# In[41]:


#plotting a visualization. Default is line plot or type = line
#style changed

df.plot(title = 'Ice Cream Ratings', xlabel = 'Daily Rating', ylabel = 'Scores')


# In[15]:


#bar charts. Can be stacked or not
#can specify a column

df['Flavor Rating'].plot(kind = 'bar', stacked = True)


# In[16]:


#horizontal bar chart
df.plot.barh(stacked = True)


# In[20]:


#scatter plots
# x & y need to be specified as columns
# scale and color can be changed
df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 100, c = 'yellow')


# In[23]:


#histagram
df.plot.hist(bins = 5)


# In[24]:


#box plots with graph candles
df.boxplot()


# In[28]:


#area chart. Can have size specified
df.plot.area(figsize = (10,5))


# In[33]:


df.plot.pie(y = 'Flavor Rating', figsize = (10, 10))


# In[ ]:




