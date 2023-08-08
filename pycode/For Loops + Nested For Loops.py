#!/usr/bin/env python
# coding: utf-8

# In[1]:


intergers = [1,2,3,4,5]


# In[2]:


for number in intergers:
    print(number)


# In[3]:


for number in intergers:
    print('yep')


# In[4]:


for Jelly in intergers:
    print(Jelly + Jelly)


# In[5]:


ice_cream_dict = {'name':'Artur Freires', 'job':'Data Analyst', 'favorite games':['diablo', 'final fantasy']}


# In[7]:


for cream in ice_cream_dict.values():
    print(cream)


# In[8]:


for key, value in ice_cream_dict.items():
    print(key,'->', value)


# In[9]:


flavors = ['Vanilla', 'Chocolate', 'Cookie Dough']
toppings = ['Hot Fudge', 'Marshmellow', 'Oreos']


# In[11]:


for one in flavors:
    for two in toppings:
        print(one,'topped with',two )


# In[ ]:




