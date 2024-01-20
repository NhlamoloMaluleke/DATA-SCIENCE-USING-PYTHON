#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib as mpl
import matplotlib.pyplot as plt


# In[2]:


import numpy as np
import pandas as pd 


# In[3]:


df_can = pd.read_excel("Canada.xlsx",sheet_name = "Canada by Citizenship",
skiprows=range(20),
skipfooter=2)
      


# In[4]:


df_can.head(5)


# In[5]:


df_can.info(verbose = False)


# In[6]:


df_can.columns.tolist()


# In[7]:


df_can.index.tolist()


# In[8]:


df_can.shape


# In[9]:


# in pandas axis=0 represents rows (default) and axis=1 represents columns.
#df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis = 1 , inplace = True)
df_can.head(2)


# In[10]:


df_can.shape


# In[11]:


df_can.head


# In[12]:


#rename the columns
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region' }, inplace= True)
df_can.columns


# In[13]:


df_can['Total'] =df_can.sum(axis=1, numeric_only= True)


# In[14]:


df_can.head(2)


# In[15]:


#We can check to see how many null objects we have in the dataset as follows

df_can.isnull().sum()


# In[16]:


df_can.describe()


# In[17]:


#Select multiple Columns
df_can[['Country',1980, 1981, 1982, 1983, 1984, 1985]]


# In[18]:


#select row 
#  df.loc[label]    filters by the labels of the index/column
# df.iloc[index]   filters by the positions of the index/column
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()
df_can.set_index('Country', inplace = True)


# In[19]:


df_can.head(3)


# In[20]:


df_can.reset_index()


# In[21]:


# optional: to remove the name of the index
#df_can.index.name = 'Country'


# In[22]:


#Let's view the number of immigrants from Japan (row 87) for the following scenarios
#1. The full row data (all columns)
df_can.loc['Japan']


# In[23]:


#2 For year 2013
df_can.loc['Japan', 2013]


# In[24]:


#For years 1980 to 1985
# add anpther parenthese for a range of columns
df_can.loc['Japan', [1980,1981,1982,1983,1984,1985]]


# In[25]:


#let's convert the column names into strings:
df_can.columns = list(map(str,df_can.columns))


# In[26]:


#let's declare a variable that will allow us to easily call upon the full
years = list(map(str,range(1980,2014)))
years


# In[27]:


#Filtering based on a criteria
#To filter the dataframe based on a condition, we simply pass the condition as a boolean vector.
#For example, Let's filter the dataframe to show the data on Asian countries (AreaName = Asia).

# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)


# In[28]:


# 2. pass this condition into the dataFrame
df_can[condition]


# In[29]:


# we can pass multiple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia
# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses

df_can[(df_can['Continent'] == 'Asia') & (df_can['Region']=='Southern Asia')]


# In[30]:


df_can.info()


# In[31]:


haiti = df_can.loc['Haiti', years]


# In[32]:


haiti.head()


# In[33]:


haiti.plot()


# In[34]:


#let's change the type of the index values to integer for plotting.
haiti.index = haiti.map(int)
haiti.plot(kind ='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of imigrants')
plt.xlabel('Years')
plt.show()


# In[ ]:





# In[36]:


#**Question:** Let's compare the number of immigrants from India and China from 1980 to 2013.
#Step 1: Get the data set for China and India, and display the dataframe.

df_chi = df_can.loc[['India','China'], years]


# In[37]:


#Step 2: Plot graph. We will explicitly specify line plot by passing in kind parameter to plot().
df_chi.plot(kind = 'line')


# In[38]:


df_chi = df_chi.transpose()
df_chi.head()


# In[39]:


df_chi.index = df_chi.index.map(int)
df_chi.plot(kind='bar')
plt.title('Immigration from China and India')
plt.ylabel('Number of imigrants')
plt.xlabel('Years')
plt.show()


# In[40]:


print(type(haiti))
print(haiti.head(5))


# In[41]:


#Compare the trend of top 5 countries that contributed the most to immigration to Canada.
#Step 1: Get the dataset. Recall that we created a Total column that calculates cumulative immigration by country. 
#We will sort on this column to get our top 5 countries using pandas sort_values() method.
#inplace = True # paramemter saves the changes to the original df_can dataframe
df_can.sort_values(by ='Total',ascending=False, axis = 0 ,inplace=True)



# In[42]:


# get the top 5 counties 
df_top5 = df_can.head(5)
print(df_top5)


# In[43]:


# transpose the dataframe
df_top5 = df_top5[years].transpose()
print(df_top5)


# In[44]:


#Step 2: Plot the dataframe. To make the plot more readeable, we will change the size using the `figsize` parameter.
df_top5.index = df_top5.index.map(int)


# In[45]:


#let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='area',figsize=(14,8)) # pass a tuple (x, y) size
plt.title('Immigration top 5')
plt.ylabel('Number of imigrants')
plt.xlabel('Years')
plt.show()


# In[49]:


count, bin_edges = np.histogram(df_can['2013'])
df_can['2013'].plot(kind= 'area', xticks= bin_edges)
plt.title('Histogram of immigration from 195 countries in 2013')
plt.ylabel('Number of counties')
plt.xlabel('Number of immigrants')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[47]:





# In[ ]:





# In[ ]:





# In[ ]:




