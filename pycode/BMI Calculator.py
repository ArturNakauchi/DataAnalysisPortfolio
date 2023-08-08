#!/usr/bin/env python
# coding: utf-8

# In[5]:


#BMI = (weight in pounts x 703) / (height in inches x height in inches)
# < 16.0	Severely Underweight
# 16.0 - 18.4	Underweight
# 18.5 - 24.9	Normal
# 25.0 - 29.9	Overweight
# 30.0 - 34.9	Moderately Obese
# 35.0 - 39.9	Severely Obese
# > 40.0	Morbidly Obese


# In[10]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))


BMI = (weight * 703) / (height * height)
print('Your BMI is: ', BMI)

if BMI >0:
    if(BMI<18.5):
        print(name +", You are Underweight")
    elif(BMI<=24.9):
        print(name + ", You are Normal")
    elif(BMI<29.9):
        print(name + ", You are Overweight")
    elif(BMI<34.9):
        print(name + ", You are Obese")
    elif(BMI<39.9):
        print(name + ", You are Severely Obese")      
    else:
        print(name + ", You are Morbidly Obese")
else:
    print("Please a valid input")


# In[ ]:



        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




