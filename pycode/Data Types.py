#!/usr/bin/env python
# coding: utf-8

# In[1]:


type(- 12 + 100)


# In[2]:


type(12 + 10.25)


# In[3]:


type(12 + 3j)


# In[6]:


#Boolean

type(True)
type(False)
type(1>5)


# In[7]:


1 > 5


# In[8]:


#Strings
'Single Quote'


# In[9]:


"Double Quote"


# In[19]:


multiline="""
Long text
I'm a poet
I can write single and double quotes here
"Like this" or like 'this'
because I can
"""


# In[20]:


print(multiline)


# In[21]:


type(multiline)


# In[22]:


a = 'Hello World!'


# In[23]:


print(a[1:5])


# In[24]:


print(a[0])


# In[25]:


print(a[:5])


# In[26]:


print(a[:-4])


# In[27]:


print(a[-4])


# In[28]:


a*3


# In[29]:


a + a


# In[30]:


#List
[1,2,3]


# In[31]:


['Strawberry', 'Cookie Dough', 'Chocolate']


# In[32]:


['Vanilla', 3, ['Scoops', 'Spoon'], True]


# In[35]:


ice_cream = ['Strawberry', 'Cookie Dough', 'Chocolate']
ice_cream.append('Salted Caramel')
ice_cream


# In[36]:


ice_cream[0] = 'Butter Pecan'
ice_cream


# In[37]:


nest_list = ['Vanilla', 3, ['Scoops', 'Spoon'], True]


# In[41]:


nest_list[2]


# In[42]:


nest_list[2][1]


# In[44]:


#Tuple

tuple_scoops = (1, 2, 3, 2, 1)


# In[45]:


type(tuple_scoops)


# In[46]:


tuple_scoops[0]


# In[50]:


#Sets

daily_pints = {1,2,3}


# In[51]:


type(daily_pints)


# In[52]:


print(daily_pints)


# In[66]:


daily_pints_log = {1,2,31,2,3,4,5,6,7}
print(daily_pints_log)


# In[65]:


second_daily_pints_log = {1,2,4,4,5,6,7,32}
print(second_daily_pints_log)


# In[67]:


#Finding unique values between the two sets
daily_pints_log | second_daily_pints_log


# In[68]:


#Shows the ones that appear in both sets
print(daily_pints_log & second_daily_pints_log)


# In[69]:


#Subtracting the ones that are the same. The ones that do not match
print(daily_pints_log - second_daily_pints_log)


# In[70]:


#Show the ones that are unique to their sets. Values that are in one or the other, but not in both.
print(daily_pints_log ^ second_daily_pints_log)


# In[71]:


#Dictionaries
#Key/Value Pair

dict_cream = {'name':'Artur Freires', 'weekly wage': 2, 'favorite game':['diablo2', 'pokemon gold']}


# In[72]:


type(dict_cream)


# In[73]:


dict_cream.values()


# In[74]:


dict_cream.keys()


# In[75]:


dict_cream.items()


# In[76]:


dict_cream['name']


# In[77]:


dict_cream['name'] = 'Artur F Freires'


# In[78]:


dict_cream['name']


# In[79]:


dict_cream.update({'name':'Artur Freires', 'weekly wage': 2, 'favorite game':['final fantasy', 'gundam'], 'more favorite game':'total war'})


# In[80]:


dict_cream.values()


# In[81]:


del dict_cream['weekly wage']
print(dict_cream)


# In[ ]:




