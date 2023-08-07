#!/usr/bin/env python
# coding: utf-8

# In[1]:


if 25 > 10:
    print('It worked!')


# In[2]:


if 25 > 10:
    print('It worked!')
else:
    print('It did not work...')


# In[3]:


if (25 < 10) or (1 < 3):
    print('It worked!')
elif 25 < 20:
    print('elif worked!')
elif 25 < 21:
    print('elif 2 worked!')
elif 25 < 40:
    print('elif 3 worked!')
elif 25 < 50:
    print('elif 4 worked!')
else:
    print('It did not work...')


# In[4]:


print('It worked!') if 10>30 else print('It did not work...')


# In[5]:


if (25 < 10) or (1 < 3):
    print('It worked!')
    if 10 > 5:
        print('This nested if statement worked!')
elif 25 < 20:
    print('elif worked!')
elif 25 < 21:
    print('elif 2 worked!')
elif 25 < 40:
    print('elif 3 worked!')
elif 25 < 50:
    print('elif 4 worked!')
else:
    print('It did not work...')


# In[ ]:




