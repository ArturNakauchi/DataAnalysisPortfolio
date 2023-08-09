#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = "https://www.scrapethissite.com/pages/forms/"


# In[3]:


page = requests.get(url)


# In[4]:


soup = BeautifulSoup(page.text, 'html')


# In[5]:


print(soup)


# In[6]:


soup.find('div')


# In[15]:


#pulling just the initial paragraph

soup.find_all('p', class_ = 'lead')


# In[17]:


#findall doesn't fetch text data. Find needs to be used instead
#strip() cleans a bit more of the information

soup.find('p', class_ = 'lead').text.strip()


# In[19]:


soup.find_all('td', class_ = 'name')


# In[ ]:




