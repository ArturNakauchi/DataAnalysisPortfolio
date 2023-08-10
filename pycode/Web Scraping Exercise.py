#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[5]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[6]:


print(soup)


# In[10]:


soup.find_all('table', class_ = 'wikitable sortable')


# In[11]:


table = soup.find_all('table')[1]


# In[12]:


print(table)


# In[18]:


world_titles = table.find_all('th')


# In[14]:


world_titles


# In[19]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[21]:


import pandas as pd


# In[23]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[26]:


column_data = table.find_all('tr')
column_data


# In[29]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    lenght = len(df)
    df.loc[lenght] = individual_row_data


# In[30]:


df


# In[32]:


df.to_csv(r'C:\Users\Artur\Desktop\Python_Projects\TestFolder\Companies.csv', index = False)


# In[ ]:




