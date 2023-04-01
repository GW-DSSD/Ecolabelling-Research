import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot

data = pd.read_csv('Building_Energy_Benchmarking.csv')

print(len(data.columns))
# print(data.info())

# CITY
# STATE
# UBID
# OBJECTID
# LATITUDE
# LONGITUDE
# PMPROPERTYID
# REPORTEDADDRESS

df = data.drop(['CITY', 'STATE', 'UBID', 'OBJECTID',
                'LATITUDE', 'LONGITUDE', 'PMPROPERTYID', 'REPORTEDADDRESS'], axis=1)
print(len(df.columns))
