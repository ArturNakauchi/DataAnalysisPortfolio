#!/usr/bin/env python
# coding: utf-8

# ## Automated File Sorter

# In[1]:


import os, shutil


# In[6]:


path = r"C:/Users/Artur/Desktop/Python_Projects/TestFolder/"


# In[21]:


#shows the files in the path

os.listdir(path)


# In[22]:


#save the path in a variable
file_name = os.listdir(path)


# In[23]:


#create the folders
folder_names = ['csv files', 'image files', 'text files']

#go through the array of range. Create 3 folders based on the string array
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])
        
#checks if the file type is in the folder
#"path + "csv files/" + file" and similars are the current folders being checked in the for loop
#shutil moves the file

for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)


# In[15]:





# In[ ]:




