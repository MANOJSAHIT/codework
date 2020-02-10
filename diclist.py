#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
dic={}
l1=[]
n=int(input('enter the number of categories: '))
n1=int(input('enter the number of elements under each category: '))
for i in range(n):
    k=input('enter the names of category: ')
    l1.append([])
    for j in range(n1):
        l1[i].append(input('enter the data under that category: '))
        dic[k]=l1[i]
print(pd.DataFrame(dic,index=range(n1)))


# In[19]:


print(dic.get('apple'))


# In[ ]:




