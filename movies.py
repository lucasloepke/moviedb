import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import json
import os; os.chdir(os.path.dirname(__file__))

class bc:
    HEADER = '\033[95m'
    b = '\033[94m'
    c = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#---------------------------------------------------------------------------
# note that dataset does not cover movies newer than 2016

def extract_genres(genres_str, limit=None):
    try:
        genres = json.loads(genres_str)
        genre_names = [genre['name'] for genre in genres]
        if limit:
            genre_names = genre_names[:limit]  # Limit the number of genres if specified
        return ", ".join(genre_names)  # Join multiple genres with a comma
    except (json.JSONDecodeError, TypeError, KeyError):
        return "N/A"

#---------------------------------------------------------------------------
df = pd.read_csv(r'tmdb_5000_movies.csv')

df['profit'] = df['revenue'] - df['budget'] # creating profit col
df['year'] = df['release_date'].str[:4] # extracting release year from date
df['Title'] = df['original_title']; df['score'] = df['vote_average'] # cleaning headers

print(f"{bc.b}---{bc.ENDC} {bc.c} Most Profitable Movies {bc.b} -------------------------------------------------------------------------{bc.ENDC}")
sdf = df[['Title', 'year', 'budget', 'revenue', 'profit', 'score']].sort_values('profit', ascending=False)
print(sdf.head(10).to_string(index=False))

print(f"{bc.b}---{bc.ENDC} {bc.c} Summary Statistics {bc.b} -----------------------------------------------------------------------------{bc.ENDC}")
# Calculate statistics
mean_score = df['score'].mean()
mean_revenue = df['revenue'].mean()
mean_profit = df['profit'].mean()
# Print fun facts
print(f"Average score: {mean_score:.2f}", end="\t\t")
print(f"Average revenue: ${mean_revenue/1e6:.2f}m", end="\t\t")
print(f"Average profit: ${mean_profit/1e6:.2f}m")

print(f"{bc.b}---{bc.ENDC} {bc.c} Most Profitable Years {bc.b} --------------------------------------------------------------------------{bc.ENDC}")
print(sdf.groupby(['year']).sum().sort_values('profit', ascending=False)['profit'].head(4).apply(lambda x: '{:.1f} billion'.format(x / 1e9)).to_string(header=False))

print(f"{bc.b}---{bc.ENDC} {bc.c} Biggest Flops {bc.b} ----------------------------------------------------------------------------------{bc.ENDC}")
print(sdf.tail(5).to_string(index=False))

print(f"{bc.b}---{bc.ENDC} {bc.c} Harry Potter Series {bc.b} ----------------------------------------------------------------------------{bc.ENDC}")
# For some reason the Deathly Hallows aren't included in this dataset so I will add them.
sdf.loc[-1] = ["Harry Potter and the Deathly Hallows: Part 1", 2010, 125e6, 980e6, 980e6-125e6, 7.7]  # adding a row
sdf.loc[-2] = ["Harry Potter and the Deathly Hallows: Part 2", 2010, 125e6, 1340e6, 1340e6-125e6, 8.1]  # adding a row
# ensuring years are numeric, not text
sdf['year'] = pd.to_numeric(sdf['year'], errors='coerce')
pd.options.display.float_format = '{:.2f}'.format
# formatting all following sdf prints
sdf['budget'] = sdf['budget'].apply(lambda x: '{:.0f}m'.format(x/1e6))
sdf['revenue'] = sdf['revenue'].apply(lambda x: '{:.0f}m'.format(x/1e6))
sdf['profit'] = sdf['profit'].apply(lambda x: '{:.0f}m'.format(x/1e6))
sdf['year'] = sdf['year'].apply(lambda x: '{:.0f}'.format(x))
sdf['score'] = sdf['score'].apply(lambda x: '{:.1f}'.format(x))
print(sdf[sdf['Title'].str.contains('Harry Potter')].sort_values('year').to_string(index=False))

print(f"{bc.b}---{bc.ENDC} {bc.c} Middle Earth {bc.b} -----------------------------------------------------------------------------------{bc.ENDC}")
print(sdf[sdf['Title'].str.contains('Lord of the Rings|Hobbit')].sort_values('year').to_string(index=False))

print(f"{bc.b}---{bc.ENDC} {bc.c} Batman {bc.b} -----------------------------------------------------------------------------------------{bc.ENDC}")
print(sdf[sdf['Title'].str.contains('Batman|Dark Knight')].sort_values('year').to_string(index=False))

print(f"{bc.b}---{bc.ENDC} {bc.c} Most Popular Films {bc.b} -----------------------------------------------------------------------------{bc.ENDC}")
ssdf = df[['Title', 'year','profit', 'score', 'popularity']].sort_values('popularity', ascending=False)
ssdf['profit'] = ssdf['profit'].apply(lambda x: '{:.0f}m'.format(x/1e6))
print(ssdf.head(5).to_string(index=False))

print(f"{bc.b}---{bc.ENDC} {bc.c} JSON Items {bc.b} -------------------------------------------------------------------------------------{bc.ENDC}")
fdf = df[['Title', 'year', 'genres', 'keywords', 'production_companies', 'profit']].sort_values('profit', ascending=False)
fdf['genres'] = df['genres'].apply(lambda x: extract_genres(x, limit=2))
fdf['keywords'] = fdf['keywords'].apply(lambda x: extract_genres(x, limit=3))
fdf['production_companies'] = fdf['production_companies'].apply(lambda x: extract_genres(x, limit=1))
fdf['profit'] = fdf['profit'].apply(lambda x: '{:.0f}m'.format(x/1e6))
print(fdf.head(7).to_string(index=False))
print(f"{bc.b}------------------------------------------------------------------------------------------------------{bc.ENDC}")