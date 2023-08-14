#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df = pd.read_csv(r"C:\Users\Artur\Desktop\Python_Projects\world_population.csv")
df


# In[6]:


#assign the country column as the index

df = pd.read_csv(r"C:\Users\Artur\Desktop\Python_Projects\world_population.csv", index_col = "Country")


# In[7]:


df


# In[33]:


#resetting index to default numbers

df.reset_index(inplace=True)
df


# In[35]:


#another way of saving the column index. inplace saves the new index to the same variable

#df.set_index('Country', inplace = True)

#df


# In[11]:


#location of data based on the current index

df.loc['Albania']


# In[13]:


#location of data based on the original numerical index

df.iloc[1]


# In[22]:


df.reset_index(inplace = True)


# In[19]:


df


# In[34]:


#setting up multiple indexes

df.set_index(['Continent','Country'], inplace = True)

pd.set_option('display.max.rows',235)


# In[24]:


df


# In[37]:


#sorting based on
df.sort_index(ascending = [False, True])


# In[38]:


#this won't return data. It will return a indexed table instead due to the new index structure
df.loc['Africa']


# In[39]:


#in this case, with newly created indexes, a loc that returns data would have to include both

df.loc['Africa','Angola']


# In[42]:


#this still would go straight for the integer index
df.iloc[1]


# In[ ]:




