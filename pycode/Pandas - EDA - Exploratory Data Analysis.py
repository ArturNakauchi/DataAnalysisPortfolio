#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv(r"C:\Users\Artur\Desktop\Python_Projects\world_population_new.csv")
df


# In[4]:


#lambda function used to change the number of digits after float digits
pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[9]:


#A good practice is to check the information for the table
df.info()


# In[10]:


#Same for describe
df.describe()


# In[13]:


#this checks for empty fields of data

df.isnull().sum()


# In[15]:


#checking for coherence. unique countries, the number of continents
df.nunique()


# In[19]:


#checking the countries with the lowest/highest population
df.sort_values(by='World Population Percentage', ascending = False).head(10)


# In[20]:


#looking at correlations
df.corr()


# In[25]:


#seaborn creates a heatmap
sns.heatmap(df.corr(numeric_only = True), annot = True)

#changes the dimensions for better visualization
plt.rcParams['figure.figsize'] = (20,7)

#shows the plot
plt.show()


# In[31]:


#there are certain continents that grew more than others. How do we check this?
#start with groupby()

df.groupby('Continent').mean(numeric_only = True).sort_values(by = "2022 Population", ascending = False)


# In[28]:


#checking for a specific continent
df[df['Continent'].str.contains('Oceania')]


# In[39]:


#creating a new data frame for visualization. Selecting only the populations columns. 
#THIS IS THE EASY, BUT NOT IDEAL WAY TO DO IT
#df2 = df.groupby('Continent')[df.columns[5:13]].mean(numeric_only = True).sort_values(by = "2022 Population", ascending = False)

#A better way to visualize the data in order, is to put the years in the ascending order manually
df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean(numeric_only = True).sort_values(by = "2022 Population", ascending = False)
df2


# In[37]:


#easy shortcut to copy and paste the columns. Or I can use df.columns[5:13]
df.columns


# In[40]:


#creating a new dataframe with a transposed index columns
df3 = df2.transpose()


# In[41]:


df3


# In[42]:


#the plot is now in ascending order and indicates the growth of every continent
df3.plot()


# In[44]:


# how to check for outliers (abnormal data, the dots/circles)
df.boxplot(figsize = (20,10))


# In[47]:


#selecting data types that are only numbers. Can be used as include = object. Can be useful when filtering data
df.select_dtypes(include = 'number')


# In[ ]:




