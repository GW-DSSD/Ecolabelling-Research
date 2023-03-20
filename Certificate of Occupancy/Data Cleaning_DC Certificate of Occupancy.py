# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%%[markdown]'

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

import pandas as pd
import re

df = pd.read_csv('Certificate_of_Occupancy.csv')
df = df[df['DESCRIPTION_OF_OCCUPANCY'].notnull()]
df['CLEANED_DESCRIPTION_OF_OCCUPANCY'] = df['DESCRIPTION_OF_OCCUPANCY'].str.lower().apply\
(lambda x: re.findall(r'\b(restaurant|office|apartment|gas|gasoline|flat|residential|retail|drycleaning|prepared food|school)\b', x))

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
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'DRYCLEANING' in x), 'CATEGORY'] = 'drycleaning'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'PREPARED FOOD' in x), 'CATEGORY'] = 'prepared food shop'
df.loc[df['CLEANED_DESCRIPTION_OF_OCCUPANCY'].apply(lambda x: 'SCHOOL' in x or 'KINDERGARTEN' in x), 'CATEGORY'] = 'school'

# Save the standardized data set
df.to_csv('Standardized_Certificate_of_Occupancy.csv', index=False)


# %%
