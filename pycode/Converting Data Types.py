#!/usr/bin/env python
# coding: utf-8

# In[1]:


num_int = 7
type(num_int)


# In[2]:


num_str = '7'
type(num_str)


# In[3]:


num_str_conv = int(num_str)
type(num_str_conv)


# In[4]:


num_sum = num_int + num_str_conv
print(num_sum)


# In[5]:


type(num_sum)


# In[6]:


list_type = [1,2,3,4,5]
type(list_type)


# In[7]:


type(tuple(list_type))


# In[8]:


list_type = [2,3,4,5,5,5,6,7,7,8]


# In[9]:


type(set(list_type))


# In[10]:


dict_type = {'name':'Artur', 'age':'33', 'last name':'freires'}
type(dict_type)


# In[11]:


dict_type.items()


# In[12]:


dict_type.values()


# In[13]:


dict_type.keys()


# In[14]:


type(list(dict_type.values()))


# In[15]:


type(list(dict_type.keys()))


# In[16]:


long_str = 'I like cake'
list(long_str)


# In[ ]:




