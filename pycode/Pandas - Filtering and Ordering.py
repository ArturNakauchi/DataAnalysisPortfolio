#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\Artur\Desktop\Python_Projects\world_population.csv")


# In[4]:


df


# In[6]:


#filtering by column

df[df['Rank'] <= 10]


# In[9]:


#looking for specific rows

specific_countries =  ['Bangladesh', 'Brazil']

df[df['Country'].isin(specific_countries)]


# In[12]:


#search for a specific term or string inside the data

df[df['Country'].str.contains('United')]


# In[14]:


#Use Country as an index

df2 = df.set_index('Country')
df2


# In[20]:


#Filter through axis and specific columns

df2.filter(items = ['Continent','CCA3'], axis = 1)


# In[21]:


df2.filter(items = ['Zimbabwe'], axis = 0)


# In[23]:


df2.filter(like = 'United', axis = 0)


# In[24]:


df2.loc['United States']


# In[26]:


df2.iloc[3]


# In[34]:


#order by

df[df['Rank'] < 10].sort_values(by = ['Continent','Country'], ascending = [False, True])


# In[ ]:




