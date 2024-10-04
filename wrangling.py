import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
Interesting Variables:
MSSubClass (cat): Identifies the type of dwelling involved in the sale
    1-STORY 1946 & NEWER ALL STYLES ... 2 FAMILY CONVERSION - ALL STYLES AND AGES
MSZoning (cat): Identifies the general zoning classification of the sale
    Agriculture
    Commercial
    Floating Village Residential
    Industrial
    Residential High Density
    Residential Low Density Park
    Residential Medium Density
LotFrontage (num): Linear feet of street connected to property
LotArea (num): Lot size in square feet
Street (cat): Type of road access to property (Gravel or Paved)
LotShape (cat): General shape of property (Regular ... Irregular)
LandContour (cat): Flatness of the property (Level ... Depression)
Utilities (cat): Type of utilities available (All ... Electricity Only)
Neighborhood (cat): Physical locations within Ames city limits (Bloomington Heights ... Veenker)
Condition1 (cat): Proximity to various conditions (Adjacent to arterial street ... East-West Railroad)
BldgType (cat): Type of dwelling (Single-family ... Townhouse)
HouseStyle (cat): Style of dwelling (One story ... Split Level)
OverallQual (cat): Rates the overall material and finish of the house (1-10)
OverallCond (cat): Rates the overall condition of the house (1-10)
YearBuilt (num): Original construction date
"""

# I will focus on Utilities, Neighborhood, HouseStyle, and YearBuilt
df = pd.read_csv('./housing data/train.csv')

print(df.head(), '\n')
print(df['Utilities'].unique(), '\n')   # All variables are clean
print(df['Neighborhood'].unique(), '\n')
print(df['HouseStyle'].unique(), '\n')
print(df['YearBuilt'].unique(), '\n')

# Describe numeric variables
print(df['YearBuilt'].describe(), '\n')  # 75% built in 2000, min built in 1872, max built in 2010

# Finding meaningful relationships using cross tabulation
# Utilities vs. Neighborhood
utilities_neighborhood_ct = pd.crosstab(df['Utilities'], df['Neighborhood'])  # Most neighborhoods are 'AllPub', urban
print(utilities_neighborhood_ct, '\n')

# YearBuilt vs. HouseStyle
yearbuilt_housestyle_ct = pd.crosstab(df['YearBuilt'], df['HouseStyle'])  # 1/2-story houses rise mid 20th century, 1.5/2.5 less common
print(yearbuilt_housestyle_ct)

# Neighborhood vs. HouseStyle
neighborhood_housestyle_ct = pd.crosstab(df['Neighborhood'], df['HouseStyle'])  # Certain neighborhoods have clear preferences for specific house styles
print(neighborhood_housestyle_ct)

# Utilities vs. HouseStyle
utilities_housestyle_ct = pd.crosstab(df['Utilities'], df['HouseStyle'])  # Nearly all house styles are 'AllPub'
print(utilities_housestyle_ct)

# Plots
# Utilities Bar Plot
df['Utilities'].value_counts().plot(kind='bar')
plt.title('Count of Houses by Utilities')
plt.xlabel('Utilities')
plt.ylabel('Number of Houses')
plt.xticks(rotation=0)
plt.show()

# Year Built Histogram
plt.figure(figsize=(10, 5))
df['YearBuilt'].plot(kind='hist', bins=30)
plt.title('Distribution of Houses by Year Built')
plt.xlabel('Year Built')
plt.ylabel('Number of Houses')
plt.show()

# Neighborhood Bar Plot
df['Neighborhood'].value_counts().plot(kind='bar')
plt.title('Count of Houses by Neighborhood')
plt.xlabel('Neighborhood')
plt.ylabel('Number of Houses')
plt.show()

# HouseStyle Bar Plot
df['HouseStyle'].value_counts().plot(kind='bar')
plt.title('Count of Houses by House Style')
plt.xlabel('House Style')
plt.ylabel('Number of Houses')
plt.xticks(rotation=0)
plt.show()

# Mean Sales Price x House Style
housestyle_price = df.groupby('HouseStyle')['SalePrice'].agg(['mean', 'median', 'count']).sort_values(by='mean', ascending=False)

plt.figure(figsize=(10, 5))
housestyle_price['mean'].plot(kind='bar')
plt.title('Average Sale Price by House Style')
plt.xlabel('House Style')
plt.ylabel('Mean Sale Price')
plt.xticks(rotation=0)
plt.show()

# Mean Sales Price x Neighborhood
neighborhood_price = df.groupby('Neighborhood')['SalePrice'].agg(['mean', 'median', 'count']).sort_values(by='mean', ascending=False)

plt.figure(figsize=(15, 5))
neighborhood_price['mean'].plot(kind='bar')
plt.title('Average Sale Price by Neighborhood')
plt.xlabel('Neighborhood')
plt.ylabel('Mean Sale Price')
plt.xticks(rotation=90)
plt.show()

# Mean Sales Price x Utilities
utilities_price = df.groupby('Utilities')['SalePrice'].agg(['mean', 'median', 'count']).sort_values(by='mean', ascending=False)

plt.figure(figsize=(8, 5))
utilities_price['mean'].plot(kind='bar')
plt.title('Average Sale Price by Utility Access')
plt.xlabel('Utilities')
plt.ylabel('Mean Sale Price')
plt.xticks(rotation=0)
plt.show()

# Mean Sales Price x Year Built
plt.figure(figsize=(15, 5))
plt.scatter(df['YearBuilt'], df['SalePrice'])
plt.title('Sale Price vs. Year Built')
plt.xlabel('Year Built')
plt.ylabel('Sale Price')
plt.grid(True)
plt.show()
