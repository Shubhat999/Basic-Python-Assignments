#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Write Python Programs to use various operators in Python
#Arithmetic operators
x = 20
y = 3
print("Arithmetic operators")
print('x+y=',x+y)
print('x-y=',x-y)
print('x*y=',x*y)
print('x/y=',x/y)
print('x//y=',x//y)
print('x**y=',x**y)
print("\n")
#Comparison operators
print("Comparison operators")
print('x>y is ',x>y)
print('x<y is ',x<y)
print('x==y is',x==y)
print('x!=y is',x!=y)
print('x>=y is',x>=y)
print('x<=y is',x<=y)
print("\n")
#Logical operators
a= True
b= False
print("Logical operators")
print('a and b is', a and b)
print('a or b is', a or b)
print('not a is', not a)
print("\n")
#Identity operators
a1=5
b1=5
a2='Hello'
b2='Hello'
a3=[1,2,3]
b3=[1,2,3]
print("Identity operators")
print(a1 is not b1)
print(a2 is b2)
print(a3 is b3)
print("\n")
#Membership operators
p = 'Hello world'
q={1:'a', 2:'b'}
print('H' in p)
print('hello'not in p)
print(1 in q)
print('a' in q)


# In[2]:


#2) Create list of elements and slice and dice it.
color_list=["Red", "Blue", "Black", "Green"]
print(color_list[0:2])
['Red', 'Blue']


# In[12]:


#3) Using while loop accept numbers until sum of numbers is less than 100
num = int(input("Enter any number:"))
sum = 0

while(num > 0):
    reminder = num % 100
    sum = sum + reminder
    num = num //100
    print("\n Sum of number= %d" %sum)


# In[13]:


#4) Write a python program Read & write Excel files 
from openpyxl import Workbook
import time

book = Workbook()
sheet = book.active

sheet['A1']=56
sheet['A2']=43
now = time.strftime("%x")
sheet['A3']=now
book.save("sample.xlsx")


# In[3]:


#5) Write a python program to scrape reviews from a commercial web site
from bs4 import BeautifulSoup
import urllib.request


# In[4]:


url = 'https://www.yelp.com/biz/milk-and-cream-cereal-bar-new-york?osq=Ice+Cream'


# In[5]:


ourUrl = urllib.request.urlopen(url)


# In[6]:


soup = BeautifulSoup(ourUrl,'html.parser')


# In[7]:


print(soup.prettify())  


# In[8]:


#6) Create a 3x3 matrix with values ranging from 2 to 10 using numpy
import numpy as np
x = np.arange(2,11).reshape(3,3)
print(x)


# In[9]:


#7) Write a Python program to convert a list of numeric value into a one-dimensional NumPy array
import numpy as np
l= [1,2,3,4]
print("Original List", l)
a= np.array(l)
print("One-Dimensional NumPy array", a)  


# In[10]:


#8)Write a Python program to create a null vector of size 10 and update sixth value to 11.
import numpy as np
a = np.zeros(10)
print(a)
print("Update sixth value to 11")
a[6] = 11
print(a)

