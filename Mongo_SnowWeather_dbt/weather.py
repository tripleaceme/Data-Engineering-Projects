import pandas as pd


weather_df = pd.read_csv('')


weather_df.to_csv('dbt/seeds/weather.csv', index=False)