#!/usr/bin/env python
# coding: utf-8

# In[49]:


from selenium import webdriver
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import datetime
import csv
import smtplib


# In[48]:


def check_price():
    #selecting the driver
    web=webdriver.Chrome()
    web.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
    time.sleep(1)
    
    #going through the flow on the web driver
    # 1- login = Fill email on the login page
    # 2- submit = Click the buttom element to move forward
    # 3- password = Fill the password
    # 4- submit_2 = Click the buttom element to move forward
    # 5- searchbox = Fil the item to be searched
    # 6- find =  click the buttom element to search for the item
    login=web.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[1]/input[1]')
    login.send_keys('savioria@yahoo.com.br')
    
    submit=web.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[2]/span/span/input')
    submit.click()

    password=web.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[1]/input')
    password.send_keys('Canadablade123')

    submit_2=web.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[2]/span/span/input')
    submit_2.click()

    searchbox=web.find_element(By.ID, 'twotabsearchtextbox')
    searchbox.send_keys('playstation 4')

    time.sleep(1)
    
    
    find=web.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
    find.click()

    html = web.page_source

    soup = BeautifulSoup(html, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), 'html.parser')
    
    #finding the values that are going to be inserted into a dataframe/csv
    #assign the title and price of the item to variables
    title = soup2.find('span', {"class": "a-size-medium a-color-base a-text-normal"}).get_text()
    price = soup2.find('span', {'a-offscreen'}).get_text()

    #cleaning the data
    title = title.strip()
    price = price.strip()[1:]
    
    #create a timestamp
    today = datetime.date.today()

    #creating the table structure
    header = ['Title', 'Price','Date']
    data = [title,price,today]

    #inserting the header and data into csv
    #default folder for csv is the users folder
    with open('AmazonWebScraperDS.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)


# In[ ]:


#for future reference, send an email      
def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('savioria247@gmail.com','Canadablade123')
    
    subject = "Test"
    body = " test"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'savioria247@gmail.com',
        msg
     
    )


# In[ ]:


#Running in a rudimentary timer. 86400 is a day in seconds
white(True):
    check_price()
    time.sleep(86400)


# In[46]:


#validating as a data frame that can be read with pandas
import pandas as pd

df = pd.read_csv(r'C:\Users\Artur\AmazonWebScraperDS.csv')

df


# In[32]:


# #finding the values that are going to be inserted into a dataframe

# title = soup2.find('span', {"class": "a-size-medium a-color-base a-text-normal"}).get_text()
# price = soup2.find('span', {'a-offscreen'}).get_text()


# In[33]:


# #cleaning the data

# title = title.strip()
# price = price.strip()[1:]


# In[38]:


# print(title)
# print(price)

# #check for the data type before importing to a csv
# type(price)


# In[ ]:


# #create a timestamp
# today = datetime.date.today()
# print(today)


# In[41]:


# #creating the table structure
# header = ['Title', 'Price','Date']
# data = [title,price,today]

# #inserting the header and data into csv
# #default folder for csv is the users folder
# with open('AmazonWebScraperDS.csv', 'w', newline='', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerow(data)


# In[ ]:


# #To append data to an existing csv. Use the 'a+' variable

# with open('AmazonWebScraperDS.csv', 'a+', newline='', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(data)


# In[ ]:



    

