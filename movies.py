import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os; os.chdir(os.path.dirname(__file__))

#---------------------------------------------------------------------------

df = pd.read_csv(r'tmdb_5000_movies.csv')

df['profit'] = df['revenue'] - df['budget'] # creating profit col
df['year'] = df['release_date'].str[:4] # extracting release year from date
df['Title'] = df['original_title']; df['score'] = df['vote_average'] # cleaning headers


print("--- Most Profitable Movies -------------------------------------------------------------------------")
sdf = df[['Title', 'year', 'budget', 'revenue', 'profit', 'score']].sort_values('profit', ascending=False)
print(sdf)
print("--- Most Profitable Years --------------------------------------------------------------------------")
print(sdf.groupby(['year']).sum().sort_values('profit', ascending=False)['profit'].head(4).apply(lambda x: '{:.1f} billion'.format(x / 1e9)).to_string(header=False))
print("--- Summary Statistics -----------------------------------------------------------------------------")

# Calculate statistics
mean_score = df['score'].mean()
mean_revenue = df['revenue'].mean()
mean_profit = df['profit'].mean()

# Print fun facts
print(f"Average score: {mean_score:.2f}", end="\t\t")
print(f"Average revenue: ${mean_revenue/1000000:.2f}m", end="\t\t")
print(f"Average profit: ${mean_profit/1000000:.2f}m")
