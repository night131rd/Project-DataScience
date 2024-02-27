import pandas as pd 
import matplotlib.pyplot as plt 

# read the data
netflix_df = pd.read_csv('netflix_data.csv')

# remove TV shows
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']

# keeping only the columns "title", "country", "genre", "release_year", "duration" 
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

# movies shorter than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# store colors
colors = []
# assign to 4 genres groups
for index,row in netflix_movies.iterrows():
    if 'Children' in row['genre']:
        colors.append('red')
    elif 'Documentary' in row['genre']:
        colors.append('blue')
    elif 'Stand-Up' in row['genre']:
        colors.append('purple')
    else:
        colors.append('black')
        
# assign high and width with plt.figure
fig = plt.figure(figsize=(12,8))

# scatter plot for movie duration by release years
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors, )

# assign title, xlabel, ylabel
plt.title('Movie Duration by Year of Release')
plt.xlabel('Release Year')
plt.ylabel('Duration (min)')

#show the plot
plt.show()

# are we certain that the movies are getting shorter?
answer = 'No' 