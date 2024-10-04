import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
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

df = pd.read_csv('./housing data/train.csv')
print(df.head())