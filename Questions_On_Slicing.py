#!/usr/bin/env python
# coding: utf-8

# In[2]:


x='python is a dynamic language'
print(x[0:1]+x[7:8]+x[10:11]+x[12:13]+x[20:21])
# expected output:piadl


x='python is a dynamic language'
print(x[0:2]+x[6:9]+x[9:12]+x[12:14])
# expected output:py is a dy


x='python is a dynamic language'
print(x[0:6]+x[6:10]+x[20:])
# expected output:python is langauge


x='python is a dynamic language'
print(x[0:2]+x[6:9]+x[9:12]+x[12:14]+x[19:24])
# expected output:py is a dy lang


x='python is a dynamic language'
print(x[16:19]+x[19:])
# expected output:mic language


x='python is a dynamic language'
print(x[16:19]+x[19:21])
# expected output:mic l



x='python is a dynamic language'
print(x[14:19]+x[19:22])
# expected output:namic la


x='python is a dynamic language'
print(x[4:6]+x[6:10]+x[10:12])
# expected output:on is a


x='python is a dynamic language'
print(x[12:15]+x[19:22])
# expected output: dyn la


x='python is a dynamic language'
print(x[6:10]+x[10:12]+x[12:14]+x[19:22])
# expected output:is a dy la


x='python is a dynamic language'
print(x[4:6]+x[6:10]+x[10:12]+x[12:14]+x[19:22])
# expected output:on is a dy la


x='python is a dynamic language'
print(x[0:2]+x[7:9]+x[10:11]+x[12:14]+x[20:22])
# expected output:pyisadyla


x='python is a dynamic language'
print(x[0:2]+x[7:9])
# expected output:pyis


x='python is a dynamic language'
print(x[7:9]+x[10:11])
# expected output:isa


# In[15]:


# WAP and fetch the first,middle and the last element of the 
# given string
x='python is a dynamic language'
y=print(x[0])
a=print(x[13])
b=print(x[27])


# In[10]:


# wap to convert half string in upper case
x='python is a dynamic language'

# Using upper() + slicing string
y=x[:14]+x[14:].upper()
y


# In[14]:


#WAP and fetch the first two element,middle and the last two elements from  the
# given string
x='python is a dynamic language'
y=print(x[0:2])
a=print(x[13:15])
b=print(x[26:])


# In[ ]:




