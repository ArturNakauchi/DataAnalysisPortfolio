#!/usr/bin/env python
# coding: utf-8

# In[4]:


number = 0

while number < 5:
    print(number)
    number = number + 1


# In[5]:


number = 0

while number < 5:
    print(number)
    if number == 3:
        break
    number = number + 1


# In[8]:


number = 0

while number < 5:
    print(number)
    if number == 6:
        break
    number = number + 1
else:
    print('No longer < 5')


# In[9]:


number = 0

while number < 5:
    print(number)
    if number == 3:
        continue
    number = number + 1
else:
    print('No longer < 5')


# In[11]:


number = 0

while number < 5:
    number = number + 1
    if number == 3:
        continue
    print(number)
else:
    print('No longer < 5')


# In[ ]:




