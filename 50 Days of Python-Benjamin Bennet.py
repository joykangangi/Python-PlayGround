#!/usr/bin/env python
# coding: utf-8

# # Day 1   

# In[ ]:


def divide_or_square(num): if num%5 == 0: return num ** 0.5 else: return num%5 print(divide_or_square(10))


# ## Extra challenge 

# In[15]:


def longest_value(dictionary: dict):
    key1 = max(dictionary, key = len)
    print(dictionary[key1])    
   
my_dictionary = {'fruit':'apple', 'color':'green'}
longest_value(my_dictionary)


# In[18]:


def convert_add(str_list:list):
    sum = 0
    for str in str_list:
       sum += int(str)
    print(sum)
 
my_num = ['1','3','5']
convert_add(my_num)


# In[ ]:





# In[ ]:




