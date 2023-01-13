#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Write a Pandas program to select the specified columns and rows from a given data frame.
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print("Select specific columns and rows:")
print(df.iloc[[1,3,5,6],[0,1]])


# In[2]:


#2)
#i) find the aggregations like all moments of business decisions for all columns,value counts
import numpy as np
import pandas as pd
pd.read_csv('crime_data.csv',delimiter=',')
crime_data = pd.read_csv('crime_data.csv', delimiter=',')
crime_data.count()


# In[3]:


#ii)Do the plottings like plottings like histogram, boxplot, scatterplot, barplot, piechart,dot chart
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df_rape = pd.read_csv('crime_data.csv')
df_rape.head()
df_rape['Rape'].plot(kind='hist')


# In[4]:


df_rape.boxplot(grid='false', color='blue', fontsize=10, rot=60)


# In[ ]:





# In[7]:


df_rape.plot.pie(y='Rape', figsize=(6, 6))


# In[9]:


df_rape.plot(kind='scatter', x='Rape', y='Murder')


# In[10]:


#use mtcars dataset from LMS
import pandas as pd
data = pd.read_csv("mtcars.csv")
data.head()


# In[11]:


#A) delete/ drop rows-10 to 15 of all columns
data = data.drop(data.index[range(10)])
data.head()


# In[12]:


#B)drop the disp column
data = data.drop(columns=data.columns[2])
data.head()


# In[14]:


#C)Write the forloop to get value_counts of all cloumns
for col in data:
    print('-' * 40 + col + '-' * 40 , end=' - ')
    display(data[col].value_counts().head(10))


# In[24]:


#Use Bank Dataset from LMS
#A)change all the categorical columns into numerical by creating Dummies and using label encoder.
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
df=pd.read_csv("Bank-full-_1_.csv")
df.head()


# In[27]:


new_DataM1 = df
data = pd.get_dummies(new_DataM1["marital"])
data1 = pd.get_dummies(new_DataM1["job"])


# In[28]:


data.head(5)
data1.head(5)


# In[29]:


df=df.iloc[:,:].values


# In[33]:


df


# In[42]:


marital =LabelEncoder()


# In[43]:


df[:,2]=marital.fit_transform(df[:,2])


# In[44]:


df


# In[48]:


ct=ColumnTransformer(transformers=[('encode',OneHotEncoder(),[2])],remainder='passthrough')


# In[49]:


y=ct.fit_transform(df)


# In[50]:


y


# In[51]:


y=pd.DataFrame(y)
y

