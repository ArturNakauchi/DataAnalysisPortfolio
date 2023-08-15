#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df1 = pd.read_csv(r"C:\Users\Artur\Desktop\Python_Projects\LOTR.csv")
df1


# In[7]:


df2 = pd.read_csv(r"C:\Users\Artur\Desktop\Python_Projects\LOTR 2.csv")
df2


# In[11]:


#matches the fellowshipId and puts in the same data frame
#firstName gets a column because it's not specified on "on"
df1.merge(df2, how = 'inner', on = 'FellowshipID')


# In[12]:


df1.merge(df2, how = 'inner', on = ['FellowshipID', 'FirstName'])


# In[14]:


df1.merge(df2, how = 'outer')


# In[15]:


df1.merge(df2, how = 'left')


# In[16]:


df1.merge(df2, how = 'right')


# In[17]:


#takes all values from df1 and compares one by one to df2
df1.merge(df2, how = 'cross')


# In[19]:


#join functions need a proper indexing work before they're converted to proper datasets

df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_Left', rsuffix = '_Right')


# In[22]:


#to fix this, it needs the index set to specifically choose one column to match the values
#df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_Left', rsuffix = '_Right', how = 'outer')
#the how can be specified as well

df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_Left', rsuffix = '_Right')
df4


# In[28]:


#concatenate function. Joins two data frames "on top" of each other
#pd.concat([df1,df2])

#specify the type
#pd.concat([df1,df2], join = 'inner')

#specify the join by index, like a merge
pd.concat([df1,df2], join = 'outer', axis = 1)


# In[29]:


#deprecated, but there's append as well. For now
df1.append(df2)


# In[ ]:




