# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%%[markdown]'

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv('Certificate_of_Occupancy.csv')
df = df[df['DESCRIPTION_OF_OCCUPANCY'].notnull()]
df['CLEANED_DESCRIPTION_OF_OCCUPANCY'] = df['DESCRIPTION_OF_OCCUPANCY'].str.lower().apply\
(lambda x: re.findall(r'\b(restaurant|office|apartment|apt.|gas|gasoline|flat|residential|retail|drycleaning|dry cleaning|dry cleaner|prepared food\
    |school|studio|church|condo|condominium|auto|automotive|child|manufacturing|spa|car dealership|car dealer|nail|parking|fast food|grocery)\b', x))

# Create a new column called CATEGORY
df['CATEGORY'] = ''

# Assign rows to categories based on the cleaned DESCRIPTION_OF_OCCUPANCY column
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'RESTAURANT' in x), 'CATEGORY'] = 'restaurant'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'OFFICE' in x), 'CATEGORY'] = 'office'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'APARTMENT' in x or 'APT.' in x), 'CATEGORY'] = 'apartment'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'GAS' in x or 'GASOLINE' in x), 'CATEGORY'] = 'gas station'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'FLAT' in x), 'CATEGORY'] = 'flat'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'RESIDENTIAL' in x), 'CATEGORY'] = 'residential living'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'RETAIL' in x), 'CATEGORY'] = 'retail'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'DRYCLEANING' in x or 'DRY CLEANING' in x or 'DRY CLEANER' in x), 'CATEGORY'] = 'drycleaning'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'PREPARED FOOD' in x), 'CATEGORY'] = 'prepared food shop'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'SCHOOL' in x or 'KINDERGARTEN' in x), 'CATEGORY'] = 'school'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'STUDIO' in x), 'CATEGORY'] = 'studio'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'CHURCH' in x), 'CATEGORY'] = 'church'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'CONDO' in x or 'CONDOMINIUM' in x), 'CATEGORY'] = 'condominium'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'AUTO' in x or 'AUTOMOTIVE' in x), 'CATEGORY'] = 'auto shop'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'CHILD' in x), 'CATEGORY'] = 'childcare center'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'MANUFACTURING' in x), 'CATEGORY'] = 'manufacturing'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'SPA' in x), 'CATEGORY'] = 'spa'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'CAR DEALERSHIP' in x or 'CAR DEALER' in x), 'CATEGORY'] = 'car dealership'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'NAIL' in x), 'CATEGORY'] = 'nail service'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'PARKING' in x), 'CATEGORY'] = 'parking lot'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'FAST FOOD' in x), 'CATEGORY'] = 'fast food'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'GROCERY' in x), 'CATEGORY'] = 'grocery store'

# Save the standardized data set
df.to_csv('Standardized_Certificate_of_Occupancy.csv', index=False)


# %%
