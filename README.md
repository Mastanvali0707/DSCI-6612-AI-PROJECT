# DSCI-6612-AI-PROJECT
# SPRING 2022
# SUBMISSION BY Shaik Mastanvali
# Classification of EMAIL SPAM OR NON SPAM Using Machine learning
# Overview
What is Spam Email?
Spam mails are commonly referred to as junk email or unsolicited commercial email.
Why we need to filter spam email?
Undesired use of screen space, bandwidth, storagespace.
Interferes with efficient delivery of legitimate messages
How to get rid of Spam Email?
  Block (Allow) List
•   too restrictive
•   Manual Deletion
•   time consuming, inefficient
•   Automatic Deletion
•   content based
# Learning Objective
The project's goal was to accomplish the following points. If you're looking for all of the following points in this repository, I haven't included them all. I'm working on a site on this mini project, and I'll update the link to the blog later with more information. (The major goal was to develop an end-to-end machine learning project.)

Gathering data

Descriptive Analysis

Visualization of Data

Data Preparation

Modeling of Data

Evaluation of the Model

Implementation of the Model
# Our Approch
Pre Process:

• Strip out all the HTML and XML tag and get the meaningful text.

• Get all the tokens in subject and content of email and use them for potential attribute

Training and Testing:

About 2000 spam emails and about 2000 legitimate emails as training set

• About 100 spam emails and about 100 legitimate emails as testing set

• Using logistic regression, Decision Tree and random forest to learn and classify above data sets.

# Tools 
• Python

• NumPy 

• Pandas

• Scikit-learn
# Methodology

  Business Understanding
  
• Data Collection

• Data Cleaning

• Exploratory Data Analysis

• Model Building

• Model Evaluation
# PERFORMANCE EVALUATION
  Comparing the percentage of emails that are correctly (incorrectly) classified
  
• Classifying a spam email as legitimate email is more tolerable than classifying a legitimate email as spam. So we assign different weights to 2 different misclassifying’s.

•Accuracy is used as the evaluation matrices.

• Accuracy = (TP +TN)/(TP+TN+FP+FN)

• We can improve the model by using parameter tuning




