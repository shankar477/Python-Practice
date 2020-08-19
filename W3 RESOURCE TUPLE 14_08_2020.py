#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Write a Python program to create a tuple.
x=()
print(x)


# In[6]:


#Write a Python program to create a tuple with different data types. 
x1=("shanka","rri",44)
x1


# In[8]:


#Write a Python program to create a tuple with numbers and print one item
t = 1,2,3,4,5,6
print(t[2])


# In[9]:


#Write a Python program to unpack a tuple in several variables


# In[16]:


# Write a Python program to add an item in a tuple.
t = (1,2,3,4)
t2=list(t)
t2.append(7)
tuple(t2)


# In[19]:


#Write a Python program to convert a tuple to a string
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str="".join(tup)
str


# In[24]:


#Write a Python program to get the 4th element and 4th element from last of a tuple
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tuplex[3])


# In[28]:


#Write a Python program to create the colon of a tuple


# In[31]:


#Write a Python program to find the repeated items of a tuple.
t= 2, 4, 5, 6, 2, 3, 4, 4, 7
print(t.count(4))


# In[32]:


#Write a Python program to check whether an element exists within a tuple
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("w" in tuplex)


# In[35]:


#Write a Python program to convert a list to a tuple.
a1 = [5, 10, 7, 4, 15, 3]
a2=list(a1)
a2


# In[39]:


#Write a Python program to remove an item from a tuple.
w1 = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
w2=list(w1)
w2.remove(3)
w2


# In[43]:


#Write a Python program to slice a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
tuplex[2:4]


# In[44]:


#Write a Python program to find the index of an item of a tuple.


# In[56]:


tuplex = tuple("index tuple")
print(tuplex)
tuplex.index('d')


# In[57]:


#Write a Python program to find the length of a tuple.
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
len(tuplex)


# In[58]:


#Write a Python program to convert a tuple to a dictionary.
d1 = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
{k:(k+1) for k in d1}


# In[65]:


tuplex = ((2, "w"),(3, "r"))
[dict((y,x) for x,y in tuplex)]


# In[69]:


#Write a Python program to unzip a list of tuples into individual lists.
l = [(1,2), (3,4), (8,9)]
print(list((zip(*l))))


# In[72]:


l = [(1,2), (3,4), (8,9)]
[a,b,c] =l
l1=[]
for i,j,k in zip(a,b,c):
    l1.append((i,j,k))
print(l1)


# In[84]:


#Write a Python program to reverse a tuple
tuplex=1,2,3,4,5,6,7
print(tuplex[::-1])


# In[92]:


# Write a Python program to convert a list of tuples into a dictionary
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1),("r",4),("t",7)]
[dict((x,y) for x,y in l)]#not take same key# required output not coming plz do it 


# In[94]:


l2=dict(l)
l2


# In[98]:


#Write a Python program to print a tuple with string formatting
t = (100, 200, 300)
print("the tuple is:{}".format(t))


# In[107]:


#Write a Python program to replace last value of tuples in a list.
list1=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list1[2]=(70,80,100)
list1#this is not correct way plz d it


# In[26]:


#Write a Python program to count the elements in a list until an element is a tuple.
num = [10,20,30,(10,20),40]
print("elements in a list until an element is a tuple: ",num.index((10,20)))


# In[18]:


num = [10,20,30,(10,20),40]
for i in num:
    if type(i)==tuple:
        print(num.index(i))


# In[33]:


#Write a Python program to sort a tuple by its float element.
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'),("item0","24.4")]
print( sorted(price, key=lambda x:x[1], reverse=True))


# In[41]:


#Write a Python program to remove an empty tuple(s) from a list of tuples.
q1= [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
q2=[]
for i in q1:
    if len(i)!=0:
        q2.append(i)
q1=q2
print(q1)


# In[42]:


L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


# In[ ]:




