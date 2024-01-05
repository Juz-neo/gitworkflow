#!/usr/bin/env python
# coding: utf-8

# ## 11203112
# ### MIREKU NEWTON KWAKU YEBOAH
# 
# # BIOMEDICAL ENGINEERING 
# 
#  

# In[4]:


#required Python libraries


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[6]:


dataset = pd.read_csv('red_wine.csv')


# In[7]:


dataset


# In[5]:


dataset.head(10)


# In[7]:


dataset.tail(20)


# In[6]:


dataset.info()


# In[7]:


dataset.describe()


# In[8]:


# A correlation matrix
corr_matrix = dataset.corr()

# A correlation matrix using matplotlib
plt.figure(figsize=(10, 8))
plt.imshow(corr_matrix, cmap='coolwarm', interpolation='none', aspect='auto')
plt.colorbar()
plt.xticks(range(len(corr_matrix)), corr_matrix.columns, rotation='vertical')
plt.yticks(range(len(corr_matrix)), corr_matrix.columns)
plt.title('Correlation Matrix')
plt.show()



#  # 1.   Correlation Matrix Heatmap
# the correlation heatmap reveals the relationships between all the differnt variables in the dataset.
# 
# - Alcohole and Quality show a very positve correlation.

# In[9]:


# A Distribution of Alcohol
plt.figure(figsize=(10, 6))
plt.hist(dataset['alcohol'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Alcohol')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()


# # 2. Distribution of Alcohol Content 
# 
# - The histogram below illustrates the distribution of alcohol content in the dataset. Most wines have an alcohol content between 9.4% and 9.8%.

# In[121]:


# A boxplot for Boxplot of Quality by Alcohol
plt.figure(figsize=(12, 8))
dataset.boxplot(column='quality', by='alcohol', grid=False,color='skyblue')
plt.title('Boxplot of Quality by Alcohol')
plt.suptitle('')
plt.show()


# # 3. Boxplot of Quality vs. Alcohol Content
# 
# - The boxplot visually depicts the relationship between wine quality and alcohol content.It suggests that wines with higher quality tend to have slightly higher alchole content

# In[34]:


# Histogram of pH using Matplotlib

plt.figure(figsize=(10, 6))
plt.hist(dataset['pH'], bins=10, color='salmon', edgecolor='black')
plt.title('Histogram of pH')
plt.xlabel('pH')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


#  # 4. Histogram of pH
# 
# - The histogram displays the distribution of pH values in the darkest. Most wines have a pH around 3.3

# In[33]:


# Bar chart of pH using Matplotlib
plt.figure(figsize=(8, 5))
quality_counts = dataset['quality'].value_counts().sort_index()
plt.bar(quality_counts.index, quality_counts, color='green',edgecolor='black')
plt.title('Bar Chart of Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.grid(True)
plt.show()


# #  5.  Bar Chart of Wine Quality
# 
# - The bar chart provides a count of wines for each quality rating. Most wines in the dataset have a quality rating of 5.

# In[31]:


plt.figure(figsize=(10, 6))
plt.hist(dataset['volatile acidity'], bins=10, color='Teal', edgecolor='black')
plt.title('Histogram of Volatility Acidity')
plt.xlabel('Volatility Acidity')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# # 6. Histogram of Volatility Acidity
# 
# - The histogram displays the distribution of Volatility Acidity values in the darkest. Most wines have a Volatility Acidity around 0.6

# In[110]:


# A boxplot for Boxplot of Quality by Alcohol
plt.figure(figsize=(12, 8))
dataset.boxplot(column='fixed acidity', by='residual sugar', grid=False,color='gold')
plt.title('Boxplot of residual sugar by fixed acidity')
plt.suptitle('')
plt.show()


# # 7. Boxplot of Residual sugar by Fixed acidity
# 
# - The boxplot visually depicts the relationship between wine residual sugar and fixed acidity content.It suggests that wines with higher quality tend to have slightly higher alchole content

# In[30]:


plt.figure(figsize=(10, 6))
plt.scatter(dataset['volatile acidity'], dataset['citric acid'])
plt.title('Scatter Plot between volatile acidity and Citric Acid')
plt.xlabel('volatile acidity')
plt.ylabel('Citric Acid')
plt.grid(True)
plt.show()


# # 8. Scatter Plot Diagram of Volatile acidity by Citric acid
# - This scatter plot visualizes the relationship between volatile acidity and citric acid. Each blue data point represents a pair of values. The data points roughly follow a linear trend, suggesting a positive correlation between volatile acidity and citric acid. 
# 
# 
# 

# In[29]:


# Plot a hexbin plot for visualizing the distribution of points in a scatter plot
plt.figure(figsize=(12, 8))
plt.hexbin(dataset['free sulfur dioxide'], dataset['total sulfur dioxide'], gridsize=20, cmap='Blues')
plt.title('Hexbin Plot of Free Sulfur Dioxide & Total Sulfur Dioxide')
plt.xlabel('Free Sulfur Dioxide')
plt.ylabel('Total Sulfur Dioxide')
plt.grid(True)
plt.show()


# # 9. Hexbin Plot of Free Sulfur Dioxide & Total Sulfur Dioxide
# 
# - This hexbin plot visualizes the relationship between Free Sulfur Dioxide and Total Sulfur Dioxide using hexagonal bins. The color intensity represents the frequency of data points within each bin. The gridsize parameter determines the number of hexagons. In this plot, we observe a concentration of hexagons in certain areas, indicating regions of higher data density. 
# 
# 
# 
# 

# In[25]:


# Plot a bubble chart to show relationships among three variables
plt.figure(figsize=(12, 8))
plt.scatter(dataset['density'], dataset['sulphates'], alpha=0.5)
plt.title('Bubble Chart of Density & Sulphates')
plt.xlabel('Density')
plt.ylabel('Sulphates')
plt.grid(True
        )
plt.show()


# # 10. Bubble Chart of Density & Sulphates
# 
# - This bubble chart visualizes the relationship between Density and Sulphates, with each point represented by a bubble.This type of chart is effective in displaying three dimensions of data simultaneously, allowing for the exploration of multiple variables in a single plot.

# In[103]:


# Plot a donut chart to show the proportion of each category in a categorical variable
plt.figure(figsize=(8, 8))
category_counts = dataset['quality'].value_counts()
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=100, wedgeprops=dict(width=0.2))
plt.title('Donut Chart of Quality')
plt.show()


# # 11. Donut Chart of Quality
# 
# - This chart visualizes the percentage of quality in each wine sample. 

# In[24]:


plt.figure(figsize=(10, 6))
plt.scatter(dataset['chlorides'], dataset['alcohol'],color='green')
plt.title('Scatter Plot between Chlorides and Alcohol')
plt.xlabel('Chlorides')
plt.ylabel('Alcohol')
plt.grid(True)
plt.show()


# # 12. Scatter Plot between Chlorides and Alcohol
# - This scatter plot visualizes the relationship between Chlorides and Alcohol. Each blue data point represents a pair of values. The data points roughly follow a linear trend, suggesting a positive correlation between Chlorides and Alcohol.
# 
# 
# 

# In[35]:


# A Distribution of 
plt.figure(figsize=(10, 6))
plt.hist(dataset['free sulfur dioxide'], bins=30, color='pink', edgecolor='black')
plt.title('Distribution of Free Sulfur Dioxide')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()


# # 13. Distribution of Free Sulfur Dioxide 
# 
# - The histogram below illustrates the distribution of Free Sulfur Dioxide content in the dataset. Most wines have a Free Sulfur Dioxide content between 9.4% and 9.8%.

# 
# # Dataset Overview
# 
# ## The dataset comprises information about various characteristics of wines, with each row representing a distinct wine sample. The dataset includes 12 columns, covering aspects such as acidity, sulfur dioxide levels, density, pH, alcohol content, and a quality rating.
# 
# 
# -  **Fixed Acidity**: The amount of non-volatile acids in the wine.
# - **_Volatile Acidity_**: The amount of acetic acid in the wine, which can lead to an unpleasant vinegar taste.
# - **_Citric Acid_**: The amount of citric acid in the wine, which can add freshness and flavor.
# - **_Residual Sugar_**: The amount of sugar remaining after fermentation stops.
# - **_Chlorides_**: The amount of salt in the wine.
# - **_Free Sulfur Dioxide_**: The free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion.
# - **_Total Sulfur Dioxide_**: The total amount of sulfur dioxide in the wine, including free and bound forms.
# - **_Density_**: The density of the wine.
# - **_pH_**: The pH of the wine, representing its acidity or basicity.
# - **_Sulphates_**: The amount of sulfur dioxide added to the wine.
# - **_Alcohol_**: The alcohol content of the wine.
# - **_Quality_**: A subjective rating of the wine's quality, with 5 being the lowest and 6 being the highest in the provided data.
# 
# 

# ## Statistical Summary 
# 
# - The statistical summary provides key insights into the central tendencies and variability of each numeric column. Notable observations include varying scales across columns and potential outliers, warranting a closer examination of specific features.
# 
# 

# # Basic Information
# 
# - The dataset contains 1599 entries, with no missing values. The data type is a float64, indicating a continuous and discrete variable. This foundational information helps establish the dataset's structure.
# 
# 

# # Conclusion
# 
# 
# - In conclusion, the analysis provides a multifaceted understanding of the wine dataset. The exploration of individual features, their relationships, and distribution patterns contributes to a comprehensive overview. Further investigations, potentially involving advanced statistical analyses or machine learning models, can be pursued based on these initial insights.
# 
# 

# In[ ]:




