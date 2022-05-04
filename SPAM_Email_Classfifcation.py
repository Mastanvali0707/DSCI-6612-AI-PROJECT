#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split


# In[3]:


#Step1: Load Dataset
dataframe = pd.read_csv("spam.csv")
dataframe


# In[4]:


dataframe.info()


# In[5]:


dataframe.describe()


# In[7]:


#Defining Input and output variables
x = dataframe["EmailText"]
y = dataframe["Label"]


# In[8]:


##Step2: Split in to Training and Test Data
x_train,y_train = x[0:4457], y[0:4457]
x_test, y_test = x[4457: ], y[4457: ]


# In[9]:


##Step3: Extract Features
cv = CountVectorizer()  
features = cv.fit_transform(x_train)


# In[10]:


##Step4: Build a model
model = svm.SVC()
model.fit(features,y_train)


# In[11]:


#Step5: Test Accuracy
print(model.score(cv.transform(x_test),y_test))

