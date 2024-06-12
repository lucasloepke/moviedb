import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir(os.path.dirname(__file__))

#---------------------------------------------------------------------------
# Pandas
df = pd.read_csv(r'tmdb_5000_movies.csv')
random_row = df.sample()
word = random_row.iloc[0,6]
#---------------------------------------------------------------------------

df['profit'] = df['revenue'] - df['budget']
print(df[['original_title', 'budget', 'revenue', 'profit', 'vote_average']].sort_values('profit', ascending=False).head(10))

#sns.set_theme(color_codes=True)
#tips = sns.load_dataset("tips")
#sns.regplot(x="budget", y="revenue", data=df.head(10))
#for i, row in df.iterrows():
#    plt.text(row['budget'], row['revenue'], row['title'], ha='center')
#plt.show()


