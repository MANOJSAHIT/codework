#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
a=int(input('enter number of rows in matrix: '))
b=int(input('enter number of columns in matrix: '))
arr=np.empty((a,b))
for i in range(a):
    for j in range(b):
            arr[i,j]=int(input())
print(arr)
    
        


# In[2]:


n1=int(input('enter number of rows: '))
n2=int(input('enter number of columns: '))
ar=np.ones((n1,n2))
for i in range(n1):
    for j in range(n2):
        ar[i,j]=int(input('enter the element: '))
print(ar)
    


# In[ ]:





# In[ ]:




