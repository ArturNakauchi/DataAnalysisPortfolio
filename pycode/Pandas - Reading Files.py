#!/usr/bin/env python
# coding: utf-8

# In[2]:


#always use an alias as good practice. In this case, "pd"
#files used in this can be downloaded here: https://github.com/ArturNakauchi/DataAnalysisPortfolio/tree/main/datasets

import pandas as pd


# In[13]:


#calls in csv as a dataframe
#can be used in conjunction with header & name parameters to rename the Country & Region headers

df = pd.read_csv(r"C:\Users\Artur\Desktop\Python_Projects\countries of the world.csv")
df


# In[14]:


#for txt files,pd.read_table or pd.read_csv works. read_csv might need some separators (sep) cleaning

df = pd.read_table(r"C:\Users\Artur\Desktop\Python_Projects\countries of the world.txt")
df


# In[25]:


#calling in as json

df = pd.read_json(r"C:\Users\Artur\Desktop\Python_Projects\json_sample.json")
df


# In[26]:


#calling in as excel file. Can use sheet_name parameter to specify sheet page

df2 = pd.read_excel(r"C:\Users\Artur\Desktop\Python_Projects\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')
df2


# In[24]:


#increase the limit of rows/columns being displayed

pd.set_option('display.max.rows', 235)
pd.set_option('display.max.columns', 40)


# In[27]:


df2.info()


# In[28]:


df2.shape


# In[30]:


df2.head(10)


# In[31]:


df2.tail(10)


# In[48]:


df2['Rank']


# In[52]:


df2.loc[224]


# In[41]:


df2.iloc[224]


# In[ ]:




