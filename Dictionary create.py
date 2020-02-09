#!/usr/bin/env python
# coding: utf-8

# In[17]:


a=int(input('enter the no.of categories: '))
dict={}
for i in range(a):
    k=input('enter names of category')
    v=input('enter the data in category')
    dict[k]=v
print(dict)

