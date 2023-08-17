#!/usr/bin/env python
# coding: utf-8

# In[38]:


### This is an attempt to webscraping using pre 2022 methods. It gets blocked by Response code 503 from Amazon User Agent policy

#import libraries
from bs4 import BeautifulSoup
import requests

import time
import datetime

import smtplib
import scrapy


# In[39]:


class AmazonSpider(scrapy.Spider):
   name = 'scrape laptops'
   start_urls= ["https://www.amazon.com/s?k=laptop"]
   headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
   }

   def response(self, response):
        pass


# In[40]:


url = "https://www.amazon.com/Octopath-Traveler-Wayfarers-Nintendo-Switch/dp/B07BC326XK?th=1"
page = requests.get(url)
print(page)


# In[33]:


def search_keyword(keyword):
    count_page = 0
    count_asin = 0
    while True:
        count_page += 1
        #header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            #'Accept-Language': 'en-US,en;q=0.9'}
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

        url = f'https://www.amazon.com/s?k={keyword}&page={count_page}'
        print(f'Getting page: {count_page} | {url}')
        page = requests.get(url, headers = header)
        assert page.status_code == 200
        soup = BeautifulSoup(page.content, 'lxml')
        try:
            result = soup.find('div', attrs={'class': 's-main-slot s-result-list s-search-results sg-row'}).find_all('div', attrs={'data-component-type': 's-search-result'})
        except AttributeError:
            continue
        for ids in result:
            count_asin += 1
            asin = ids['data-asin']
            url_product = f'https://www.amazon.com/dp/{asin}'
            print(f'{count_asin}.{url_product}')
        
        last_page = soup.find('li', {'class': 'a-disabled a-last'})
        if not last_page:
            pass
        else:
            break



# In[34]:


search_keyword('headphones')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[37]:


#Connecting to the website

URL = "https://www.amazon.com/Octopath-Traveler-Wayfarers-Nintendo-Switch/dp/B07BC326XK"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

page = requests.get(URL, headers = headers)

assert page.status_code == 200

#Bringing in soups to fetch batches of content in html

soup1 = BeautifulSoup(page.content, 'html.parser')

#From soup1, I can make the content more readable
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

print(soup2)


# In[29]:


# title = soup2.find(id='productTitle').get_text()

# print(title)

# Going through with the usual method doesn't work due to amazon having an anti-bot in place. Will have to find a workaround
# A Google search led me to this: https://jmalku.medium.com/how-to-build-an-amazon-product-scraper-with-bypass-bot-detection-77d26b5b9ad6


# In[ ]:




