#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\Artur\Desktop\Python_Projects/Flavors.csv")


# In[3]:


df


# In[5]:


#aggregation using the groupby function
group_by_frame = df.groupby('Base Flavor')


# In[8]:


#calculating the mean
group_by_frame.mean(numeric_only = True)


# In[10]:


#aggregating and calculating the mean in a single line

df.groupby('Base Flavor').mean(numeric_only = True)


# In[12]:


df.groupby('Base Flavor').count()


# In[13]:


df.groupby('Base Flavor').min()


# In[14]:


df.groupby('Base Flavor').max()


# In[16]:


df.groupby('Base Flavor').sum(numeric_only = True)


# In[18]:


#aggregations in multiple columns

df.groupby('Base Flavor').agg({'Flavor Rating': ['mean', 'max', 'sum'], 'Texture Rating': ['mean', 'max', 'sum']})


# In[22]:


#groupby in multiple columns

df.groupby(['Base Flavor','Liked']).agg({'Flavor Rating': ['mean', 'max', 'sum']})


# In[23]:


#display lots of common values that would normally be aggregated
df.groupby('Base Flavor').describe()


# In[ ]:




