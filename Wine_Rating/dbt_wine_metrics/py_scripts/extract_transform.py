# import libraries
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# Read data
red = pd.read_csv('dbt_wine_metrics/data/Red.csv')
rose = pd.read_csv('dbt_wine_metrics/data/rose.csv')
white = pd.read_csv('dbt_wine_metrics/data/white.csv')
sparkling = pd.read_csv('dbt_wine_metrics/data/sparkling.csv')
varieties = pd.read_csv('dbt_wine_metrics/data/varieties.csv')

# Data Transformation
red['Color'] = 'Red'
rose['Color'] = 'Rose'
white['Color'] = 'White'
sparkling['Color'] = 'Sparkling'

# Concat the wines dataset
df_wines = pd.concat([red,rose,white,sparkling], ignore_index=True)

# print out random 10 rows
#print(df_wines.head(20).sample(10))

# drop off Non Vintage wines
df_wines_vintage = df_wines[df_wines['Year'] != "N.V."]

## Extract the variety for each wine
df_wines_vintage['Variety'] = 'Unknown'
for index in df_wines_vintage.index:
    for variety in varieties['Variety']:
        if variety in df_wines_vintage.loc[index, "Name"]:
            df_wines_vintage.loc[index, 'Variety'] = variety
            break


# export the data to dbt seeds folder for further analysis
df_wines_vintage.to_csv('dbt_wine_metrics/seeds/df_wines.csv', index=None)

#print(df_wines_vintage.head())