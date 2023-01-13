#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
val = input("Input some comma-separated numbers :- ")
list = val.split(",")
tuple = tuple(list)
print('List with those numbers:',list)
print('Tuple with those numbers:',tuple)


# In[2]:


#2) Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print("%s %s"%(color_list[0],color_list[-1]))


# In[3]:


#3) Write a Python program to print the even numbers from a given list
listt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in listt:
    if num % 2 == 0:
        print(num, end=" ")

