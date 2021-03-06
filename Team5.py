#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:25:26 2019

@author: danielasantacruzaguilera
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf 
from sklearn.model_selection import train_test_split # train/test split
from sklearn.neighbors import KNeighborsRegressor
import sklearn.metrics
from sklearn.model_selection import cross_val_score

excel= 'birthweight.xlsx'

birth= pd.read_excel(excel)

print(birth.info())
print(birth.shape)
print(birth.isnull().sum().sum())

#Missing values in the columns:
print(birth.isnull().any())


#Number of  missing values we have per column:
print(birth[:].isnull().sum())

#Flagging missing values: 
for col in birth:
    if birth[col].isnull().astype(int).sum() > 0:
        birth['m_'+col] = birth[col].isnull().astype(int)
        
df_b= pd.DataFrame.copy(birth)


#Correlation matrix and heatmap
correlation = df_b.iloc[:, :-11].corr()
sns.heatmap(correlation, 
            xticklabels=correlation.columns.values,
            yticklabels=correlation.columns.values)
plt.savefig('birthWeight.png')
plt.show()
#There is no correlation between birth weight and any other variable

#Histograms
fillna= pd.DataFrame.copy(df_b)
fillna= fillna.fillna(0)

for col in fillna.iloc[:, :-11]:
    sns.distplot(fillna[col])
    plt.tight_layout()
    plt.show()


#Boxplots
for col in fillna.iloc[:, :-11]:
   fillna.boxplot(column = col, vert = False)
   plt.title(f"{col}")
   plt.tight_layout()
   plt.show()
   
#Counting non zero values per column
fillna.astype(bool).sum(axis=0)
# cigarretes has 147 nonzero values 
#drink has 16 nonzero values
#the majority of race is white 1630/1832 for father, 1624/1832 for mother

#############################################################################
#1575 women did not smoke along with 110 missing values for smoking. 
#This means 1685/1872 observations do not involve mother smoking. 
#This results in a low correlation between our birthweight and smoking
# because there is not enough data on mothers who smoke to be significant. 
#We face a similar situation with our Alcohol Variable. 
#We find 1701 mothers who do not drink alcohol and we find another 115 
#observations have missing values for alcohol. Therefore 1816/1872 
#observations do not have any impact upon low birthweight. 
#The lack of data on mothers who drank alcohol is also leading us to find 
#little correlation with birthweight.  
##############################################################################

#ANALYZING THE NEW DATASET FOR LOW BIRTHWEIGHT
birthfeature= 'birthweight_feature_set.xlsx'

df= pd.read_excel(birthfeature)

print(df.info())
print(df.shape)
print(df.isnull().sum().sum())

#Missing values in the columns:
print(df.isnull().any())

#Number of  missing values we have per column:
print(df[:].isnull().sum())

#Correlation matrix and heatmap
correlation2 = df.corr()
sns.heatmap(correlation2, 
            xticklabels=correlation2.columns.values,
            yticklabels=correlation2.columns.values)
plt.savefig('birthWeight2.png')
plt.show()

