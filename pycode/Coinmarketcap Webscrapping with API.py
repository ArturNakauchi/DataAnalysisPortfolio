#!/usr/bin/env python
# coding: utf-8

# In[30]:


#RESET

#Use this line in Anaconda Prompt to avoid getting the IOPub data error
#jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10



from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '510b2f28-9210-4af6-aced-adc51b7425e9',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

df= pd.json_normalize(data['data'])


# In[38]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#pd.set_option('display.float_format', lambda x: '%.5f' % x) #set the visualization for float numbers


# In[10]:


#RESET

#make the json more presentable
#df= pd.json_normalize(data['data'])

#create a timestamp column
# df['timestamp'] = pd.to_datetime('now')
# df


# In[31]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

def api_runner():
    
    #dataframe to be declared beforehand
    global df
    #Sandbox environment is included on the 
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'15',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '510b2f28-9210-4af6-aced-adc51b7425e9',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
#     #Previous method of concatenating data frames
#     #make the json more presentable
#     df2= pd.json_normalize(data['data'])
#     #create a timestamp column
#     df2['timestamp'] = pd.Timestamp.now()
#     #add data to a panda function and return it anew  
#     #df = pd.concat([df,df2])

    df= pd.json_normalize(data['data'])
    #create a timestamp column with the correct timestamp
    df['timestamp'] = pd.Timestamp.now(pytz.timezone('Canada/Pacific'))
    #add data to a panda function and return it anew  
    df
    
    
    #check if the outputfile exists. If it doesn't it will create it and check for the header
    if not os.path.isfile(r'C:\Users\Artur\Desktop\Python_Projects\CryptoAPI.csv'):
        df.to_csv(r'C:\Users\Artur\Desktop\Python_Projects\CryptoAPI.csv', header = 'column_names')
    else:
        df.to_csv(r'C:\Users\Artur\Desktop\Python_Projects\CryptoAPI.csv', mode = 'a', header = False) # mode = a stands for append, header check is False so it doesn't append based on headers


# In[32]:


import os
from time import time
from time import sleep
import pandas as pd
import pytz


#create the for loop to call API 
for i in range(333):
    api_runner()
    print('API Runner completed')
    sleep(60) #sleep for 1 minute
exit()


# In[33]:


result = pd.read_csv(r'C:\Users\Artur\Desktop\Python_Projects\CryptoAPI.csv')
result


# In[67]:


df


# In[68]:


#group by and average

meandf= df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d']].mean()
meandf


# In[40]:


#creating a series of data. For a different type of visualization

dfstack = meandf.stack()

dfstack


# In[41]:


#changing it back to data frame and keeping the new column structure
convstack = dfstack.to_frame(name='values')
convstack


# In[47]:


convstack


# In[42]:


#count the number of values to create an index
convstack.count()


# In[50]:


#to create an index first create an index with a range similar to the number of columns

index = pd.Index(range(90))

# indexdf = convstack.set_index(convstack['name']) #incorrect way of setting the names to index

#create a index inside the existing converted stack data frame
indexdf = convstack.set_index(index)
#reset the index to make the name column appear again
indexdf = convstack.reset_index()
indexdf


# In[53]:


#rename the incorrect column
indexdf = indexdf.rename(columns={'level_1':'percent_change'})
indexdf


# In[62]:


#replace the "quote.USD.percent_change" to something more readable
indexdf['percent_change'] = indexdf['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'], ['1h', '24h', '7d', '30d', '60d','90d'])
indexdf


# In[56]:


#creating visualizations
import seaborn as sns
import matplotlib.pyplot as plt


# In[63]:


#creating a visualization with seaborn

sns.catplot(x='percent_change',y='values', hue='name', data=indexdf, kind='point')


# In[66]:


#extracting a data specific columns and a specific coin (bitcoin)

btc_df = df[['name', 'quote.USD.price', 'timestamp']]
btc_df = btc_df.query("name == 'Bitcoin'")
btc_df


# In[69]:


sns.set_theme(style='dark')

sns.lineplot(x='timestamp', y='quote.USD.price', data = btc_df)


# In[ ]:





# In[ ]:




