# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%%[markdown]'

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import re
import seaborn as sns
df = pd.read_csv('Certificate_of_Occupancy.csv')
df = df[df['DESCRIPTION_OF_OCCUPANCY'].notnull()]

# Create a new column called CATEGORY
df['CATEGORY'] = ''

# Assign rows to categories based on the cleaned DESCRIPTION_OF_OCCUPANCY column
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('restaurant'), 'CATEGORY'] = 'restaurant'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('office'), 'CATEGORY'] = 'office'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('apt.|apartment'), 'CATEGORY'] = 'apartment'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('gas|gasoline'), 'CATEGORY'] = 'gas station'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('flat'), 'CATEGORY'] = 'flat'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('residential|cooperative'), 'CATEGORY'] = 'residential living'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('retail'), 'CATEGORY'] = 'retail'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('dry cleaning|dry cleaner|drycleaning|cleaners'), 'CATEGORY'] = 'drycleaning'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('prepared food'), 'CATEGORY'] = 'prepared food shop'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('school|kindergarten'), 'CATEGORY'] = 'school'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('studio'), 'CATEGORY'] = 'studio'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('church'), 'CATEGORY'] = 'church'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('condo|condominium'), 'CATEGORY'] = 'condominium'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('auto|automotive'), 'CATEGORY'] = 'auto shop'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('child|daycare|day care'), 'CATEGORY'] = 'childcare center'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('manufacturing'), 'CATEGORY'] = 'manufacturing'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('spa'), 'CATEGORY'] = 'spa'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('nail'), 'CATEGORY'] = 'nail service'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('parking'), 'CATEGORY'] = 'parking lot'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('fast food'), 'CATEGORY'] = 'fast food'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('cafeteria'), 'CATEGORY'] = 'cafeteria'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('financial|finance|bank'), 'CATEGORY'] = 'bank or financial firm'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('grocery|market|supermarket'), 'CATEGORY'] = 'grocery store'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('dental|dentist'), 'CATEGORY'] = 'dentist'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('cafe|coffee'), 'CATEGORY'] = 'coffee shop'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('laundromat|laundry'), 'CATEGORY'] = 'laundromat'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('beauty'), 'CATEGORY'] = 'beauty shop'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('gift'), 'CATEGORY'] = 'gift shop'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('news|newstand'), 'CATEGORY'] = 'newstand'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('education|educational|learning'), 'CATEGORY'] = 'educational center'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('pool'), 'CATEGORY'] = 'pool'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('hotel'), 'CATEGORY'] = 'hotel'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('convenience|convenient'), 'CATEGORY'] = 'convenience store'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('home|house'), 'CATEGORY'] = 'house'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('stadium'), 'CATEGORY'] = 'stadium'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('community'), 'CATEGORY'] = 'community center'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('hair|barber'), 'CATEGORY'] = 'hair salon or barber'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('contractor|contractors|contracting'), 'CATEGORY'] = 'contracting firm'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('storage'), 'CATEGORY'] = 'storage center'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('food product|food products|delicatessen'), 'CATEGORY'] = 'food products store'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('car dealership|car dealer|car sales|car'), 'CATEGORY'] = 'car dealership'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('ice cream'), 'CATEGORY'] = 'ice cream shop'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('christmas tree'), 'CATEGORY'] = 'christmas tree farm'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('carry-out|carry out'), 'CATEGORY'] = 'carry out restaurant'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('animal'), 'CATEGORY'] = 'animal care'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('print|copy'), 'CATEGORY'] = 'print and copy center'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('candy'), 'CATEGORY'] = 'candy shop'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('gym|fitness'), 'CATEGORY'] = 'gym'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('hardware'), 'CATEGORY'] = 'hardware store'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('conference'), 'CATEGORY'] = 'conference center'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('hospital|nursing'), 'CATEGORY'] = 'hospital or nursing home'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('theater'), 'CATEGORY'] = 'theater'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('shoe'), 'CATEGORY'] = 'shoe shop'
df.loc[df['DESCRIPTION_OF_OCCUPANCY'].str.lower().str.contains('art gallery'), 'CATEGORY'] = 'art gallery'



# Save the standardized data set
df.to_csv('Standardized_Certificate_of_Occupancy.csv', index=False)

# %%
df.head()
sns.heatmap(df.isnull(), cbar=False)

print(df.isnull().sum())


#WARD, PERMISSION_GRANTED_TO, TRADING_AS, FLOORS_OCCUPIED, OCCUPANCY_LOAD, PROPERTY_OWNER, OWNER_ADDRESS, B_Z_A_NUMBER, APPROVED_BUILDING_CODE_USE, APPROVED_ZONING_USE, APPLICATION_COMMENTS, EXPIRATION_DATE



# %%
#Data Cleaning

df.drop(columns='APPROVED_BUILDING_CODE_USE')
df.drop(columns='B_Z_A_NUMBER')
df.drop(columns='EXPIRATION_DATE')
df.drop(columns='PERMISSION_GRANTED_TO')
df.drop(columns='TRADING_AS')
df.drop(columns='FLOORS_OCCUPIED')
df.drop(columns='OCCUPANCY_LOAD')
df.drop(columns='PROPERTY_OWNER')
df.drop(columns='OWNER_ADDRESS')
df.drop(columns='APPROVED_ZONING_USE')
df.drop(columns='APPLICATION_COMMENTS')
df.drop(columns='EXPIRATION_DATE')
df.drop(columns='WARD')


# Replace missing values with mean 
df.fillna(df.mean(), inplace=True)
df.isnull().sum()
# %%
# df['CATEGORY'].value_counts().plot(kind='barh')
# df['DESCRIPTION_OF_OCCUPANCY'].value_counts().plot(kind='barh')
# #df['PERMIT_NUMBER'].value_counts().plot(kind='barh')

plt.hist(data=df, x='CATEGORY')
plt.tight_layout()
plt.show()


# %%
