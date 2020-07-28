#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


# In[2]:


Employee = []
Salary = []
Year = []
Sex = []

#input a text file from a directory:
#WARNING! satisfaction.txt has a header!!!
txtFile = "salary.txt"
with open(txtFile, "r") as file:
    header = file.readline() #read first line as headers
    for line in file:
        data = line.split()
        Employee.append(str(data[0])) #to store name of employee
        Salary.append(float(data[1])) #a preview of the data shows the we want NUMBERS!
        Year.append(int(data[2])) #While this will be an integer, float will give better accuracy
        Sex.append(str(data[3]))
    #file.close()

#assign list variables to DataFrame object
SalaryDataFrame = pd.DataFrame({'Employee': Employee, 'Salary': Salary, 'Year':  Year, 'Sex': Sex})


# In[3]:


SalaryDataFrame


# # Problem 1

# In[36]:


grouped=SalaryDataFrame.groupby('Sex')
print(grouped.describe())


# Interpretation:
# From the given sample of 25. We can interpret the following:
# 1) The average salaries for men are more than female
# 2) The female population has the lowest minimum and maximum salaries compared to men.
# 3) However, when we look at the standard deviation it shows that there is a lot of variability in Men salaries. Hence the mean 
# salaries may be effected since 75% of men have salaries more than 38.5k USD

# # Probelm 2

# In[37]:


grouped.boxplot()
plt.show()


# From the above box plot we can conclude:
# The range of salaries for a female is less when compared to men. The difference between the maximum and minimum salaries is more for Men. The median salary for a female is around 24k whereas for men it is 30k USD.

# # Problem 3

# In[34]:


Male=SalaryDataFrame[SalaryDataFrame.Sex=='M']
Female=SalaryDataFrame[SalaryDataFrame.Sex=='F']


# In[35]:


Male1=Male.filter(items=['Salary'])
Female1=Female.filter(items=['Salary'])


# In[36]:


SalaryDataFrame1=SalaryDataFrame.filter(items=['Salary'])
SalaryDataFrame1.sum(axis=0) #calculate the summation of total salaries


# In[37]:


Male1.sum(axis=0)/SalaryDataFrame1.sum(axis=0)


# In[38]:


Female1.sum(axis=0)/SalaryDataFrame1.sum(axis=0)


# In[7]:


txtLabels= 'Male', 'Female'
fractions = [67.7,32.3]
offsets =(0, 0.05, 0, 0)
plt.pie(fractions, labels=txtLabels,
        autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()


# Of the total expenditure of the company, the majority of the salaries are distributed to men which count to 67.7% of total salary distributed where as female employees it is 32.3%. However, the population of men is larger than the female employees in a given data set.  

# # Problem 4

# In[70]:


Male.plot.scatter(x = 'Salary', y = 'Year')
plt.show()


# In[71]:


Female.plot.scatter(x = 'Salary', y = 'Year')
plt.show()


# Interpretation: It is clearly evident that as the experience increased the Male population had a very high hike in salary whereas for female employees even after having 10 years of experience they tend to earn only around 19k USD whereas men were earning around 30k USD with the same experience.

# # Problem 5

# In[81]:


Y=[35,27,45,22,25,30,37,25,17,28,43,25,22,28,29,19,29,38,19,22,39,40,21,28,30]
u = plt.hist(Y, bins=5)
plt.xlabel("Category")
plt.ylabel("Frequency")
plt.show()


# In[4]:


SalaryDataFrame.plot.hist(bins=5)


# Yes from the Histogram it looks like it follows a Normal distribution one standard deviation away from the mean on both the sides. However, there is a variability when it is two standard deviations away from the mean to the left.

# # Problem 6

# In[77]:


Y = sm.add_constant(SalaryDataFrame['Salary'])
YoungModel = sm.OLS(SalaryDataFrame['Year'], Y).fit()
YoungModel.summary()


# In[84]:


sns.regplot('Year', 'Salary', data=SalaryDataFrame)
plt.show()


# There are many outliers for the given data i.e, a lot of points are to the right or left of the blue fit lie.  For suppose we take 0 to 5 years of experience we see that there is no fixed salary trend. The data takes high deviation which shows the line of best fit is not good.

# # Problem-7

# If I was a judge and I need to make a decision only based on the sample data given then I would be in the favor of plaintiffs(females)
# Since it is clear that even the experienced female don't make identical salaries as men. However, in the ideal world, it is hard to conclude only based on the small sample size of 25 data.
