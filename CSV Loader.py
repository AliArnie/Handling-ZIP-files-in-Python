#!/usr/bin/env python
# coding: utf-8

# In[55]:


#importing the necessary modules 
import os
import pandas as pd 
import requests
import urllib
import zipfile
from StringIO import StringIO
from datetime import date

#downloading the zip folder and extracting a csv file 
print('Download starting')
zipurl = 'https://fawn.ifas.ufl.edu/data/fawnpub/daily_summaries/2020_daily.zip'
req = requests.get(zipurl)
with open('2020-1.csv', 'w') as f:
    f.write(req.content)

print("Download Complete")


#reading the downlaoded csv file 
df = pd.read_csv(r'C:\Users\aambundo\Desktop\2020_daily\2020-1.csv')

#removing rows that have missing  values
df = df.dropna()

#filtering the date column to return dates between to user-defined dates 
df['date'] = pd.to_datetime(df['date'])
start_date = '01-01-2020'
end_date = '31-01-2020'
mask = (df['date'] > start_date) & (df['date'] <= end_date)
df = df.loc[mask]
df

#calculating the average for each station ID for the stipulated time period 
df.mean(axis = 1, skipna = True)
df.head()




  




# In[ ]:


#importing Florida shapefiles 
import shapefile
shape = shapefile.Reader("C:\Users\aambundo\Desktop\Current_Florida_Air_Quality.shp")
#first feature of the shapefile
feature = shape.shapeRecords()[0]
first = feature.shape.__geo_interface__  
print first # (GeoJSON format)
{'type': 'LineString', 'coordinates': ((0.0, 0.0), (25.0, 10.0), (50.0, 50.0))}

