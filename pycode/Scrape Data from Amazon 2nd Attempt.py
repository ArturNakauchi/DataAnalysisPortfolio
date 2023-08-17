#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Not working. It gets blocked by Response code 503 from Amazon User Agent policy


# In[4]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[5]:


url = 'https://www.amazon.com/s?k=playstation+4&crid=LX5BWKSMYMOT&sprefix=playstation+%2Caps%2C168&ref=nb_sb_noss_2'



# In[6]:


#User agents are identifiers that websites use to signify that there's a real person
header = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'})


# In[7]:


webpage = requests.get(url, headers=header)


# In[8]:


webpage


# In[ ]:





# In[ ]:




