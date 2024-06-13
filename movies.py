import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import os
os.chdir(os.path.dirname(__file__))

#---------------------------------------------------------------------------

df = pd.read_csv(r'tmdb_5000_movies.csv')

df['profit'] = df['revenue'] - df['budget'] # creating profit col
df['year'] = df['release_date'].str[:4] # extracting release year from date
df['Title'] = df['original_title']; df['score'] = df['vote_average']


print("--- Most Profitable Movies -------------------------------------------------------------------------")
sdf = df[['Title', 'year', 'budget', 'revenue', 'profit', 'score']].sort_values('profit', ascending=False).head(10)
print(sdf)
print("----------------------------------------------------------------------------------------------------")

