#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


url = "https://www.scrapethissite.com/pages/forms/"


# In[8]:


#get the url. 200 is a good response. Save the request in a variable

page = requests.get(url)


# In[10]:


#parse the information in html. Save it in a variable
soup = BeautifulSoup(page.text, 'html')


# In[11]:


type(soup)


# In[14]:


print(soup.prettify())


# In[ ]:




