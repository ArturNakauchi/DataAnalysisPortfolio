#!/usr/bin/env python
# coding: utf-8

# In[1]:


def first_func():
    print('We did it')


# In[2]:


first_func()


# In[3]:


def number_squared(number):
    print(number**2)


# In[4]:


number_squared(10)


# In[5]:


def number_squared_custom(number, power):
    print(number**power)


# In[7]:


number_squared_custom(5,3)


# In[14]:


#Arbitrary argument functions

args_tuple = (5,6,1,2,8)


def number_args(*args):
    print(args[0]*args[1])


# In[17]:


number_args(*args_tuple)


# In[20]:


def number_squared_cust(number, power):
    print(number**power)


# In[21]:


number_squared_cust(power = 5, number = 3)


# In[30]:


#Keyword Arbitrary argument functions
def number_kwarg(**number):
    print('My number is: '+ number['integer'] + ' My other number: ' + number['integer2'])


# In[31]:


number_kwarg(integer = '2309', integer2 = '3214')


# In[ ]:




