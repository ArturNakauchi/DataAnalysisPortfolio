#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


#Last_Names are not clean
#Phone_Number needs a standard
#Address needs a split
#Yes and No fields needs a standard
#Last cloumn needs to be removed

df = pd.read_excel(r"C:\Users\Artur\Desktop\Python_Projects\Customer Call List.xlsx")
df


# In[5]:


#first thing is to remove the duplicates
#last row was removed

df = df.drop_duplicates()
df


# In[6]:


#removing columns that we don't need to use. In this case Not_Useful_Column
df = df.drop(columns = 'Not_Useful_Column')
df


# In[7]:


#to clean the Last_Name, I'll use strip. lstrip() removes strings from the left. rstrip() from the right. strip() from both 
#by default strip removes white spaces
# df["Last_Name"] = df['Last_Name'].str.lstrip("...")
# df["Last_Name"] = df['Last_Name'].str.lstrip("/")
# df["Last_Name"] = df['Last_Name'].str.rstrip("_")
# strip() can be combined in a single one due to being able to receive a regular expression
df["Last_Name"] = df['Last_Name'].str.strip("123._/")
df


# In[20]:


#to clean Phone_Number we remove the characters
#replace is receiving a regular expression containing the characters that will return. 
#That includes anything but, a-z, A-Z and 0-9. Then we're replacing those exceptions with "", or nothing.
# df['Phone_Number'] = df['Phone_Number'].str.replace("[^a-zA-Z0-9]","")

# #before I can change the sequence of digits into a proper format, I need to convert it to strings to make it readable
# #by the lambda function
# df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))

# # #using a lambda function to format the sequence of digits in the way I want
# df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])

# df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '')
# df['Phone_Number'] = df['Phone_Number'].str.replace('Na--', '')
df['Phone_Number'] = df['Phone_Number'].str.replace('--', '')
df


# In[21]:


#for the address column, I'll be splitting in 3 columns using split()

df[['Street_Address','State', 'Zip_Code']] = df['Address'].str.split(',',2,expand = True)
df


# In[30]:


#replacing everything that is not a "Y" or a "N" on the Paying Customer and Do_Not_Contact columns
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No','N')

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No','N')


df


# In[34]:


df = df.replace('N/a', '')
df = df.replace('NaN', '')
#as an alternative, fillna() can be used to insert a blank space into any space that has no data
df = df.fillna('')
df


# In[ ]:


#Data is now fully clean


# ![image.png](attachment:image.png)
# 

# In[35]:


#The Do_Not_Contact that contain Y are rows to be removed. I'll use a loop to check every value in the column

for x in df.index:
    if df.loc[x,"Do_Not_Contact"] == 'Y':
        df.drop(x, inplace = True)

df


# In[36]:


#For customers that have no phone_number, remove the row entirely

for x in df.index:
    if df.loc[x,"Phone_Number"] == '':
        df.drop(x, inplace = True)

df
#df.dropna(subset='Phone_Number'), inplace = True -> Could be used as an alternative to drop null values


# In[37]:


#For better visualization, reset the index

df.reset_index(drop=True)


# In[38]:


#This is the final product. Ready to be exported

df.to_csv(r'C:\Users\Artur\Desktop\Python_Projects\TestFolder\Customer_Clean.csv', index = False)


# In[ ]:




