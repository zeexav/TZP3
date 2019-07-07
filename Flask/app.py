from flask import Flask, render_template, request
import pandas as pd
from flask import *
import numpy as np
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        movie_name = request.form['title']
        user = request.form['userId']
        user = int(user)
        data = pd.read_csv('Data/movies_bow.csv')
        movies = pd.read_csv('Data/movies_sml.csv')
        print(os.getcwd())
        #Begin Content Filtering process
        indices = pd.Series(data.index, index=data['Title'])
        idx = indices[movie_name]
        count = CountVectorizer()
        count_matrix = count.fit_transform(data['bag_of_words'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:26]
        movie_indices = [i[0] for i in sim_scores]
        content_results = pd.DataFrame(data['movieId'].iloc[movie_indices])

        # files for collaborative filtering model
        ratings = pd.read_csv('Data/ratings_sml.csv')
        preds = pd.read_hdf('Data/preds_hdf2.h5')

        #begin collaborative filtering process
        sorted_user_predictions = pd.DataFrame(preds.iloc[user].sort_values(ascending=False).reset_index())

        # Get the movies the user originally rated
        user_data = ratings[ratings.userId == user]
        user_full = (user_data.merge(movies, how = 'left', left_on = 'movieId', right_on = 'movieId').
                     sort_values(['rating'], ascending=False))
        #grab only needed columns
        user_full = user_full[['userId', 'movieId', 'Title_x', 'rating', 'genres', 'Actors', 'Director', 'Plot', 'Poster']].\
            rename(columns = {'Title_x': 'Title'})

        # set number of items to return from collaborative filter process
        num_recommendations = 1000

        # Recommend the highest predicted rating movies that the user hasn't seen yet.
        movie_preds = (movies[~movies['movieId'].isin(user_full['movieId'])].
         merge(pd.DataFrame(sorted_user_predictions).reset_index(), how = 'left',
               left_on = 'movieId',
               right_on = 'movieId').
         rename(columns = {user: 'Predictions'}).
         sort_values('Predictions', ascending = False).
                       iloc[:num_recommendations])

        #Find the similarity scores for the movies returned from the content system. 
        # Display only the highest ranked ones
        movie_recs = pd.merge(content_results, movie_preds, how='left', on='movieId').\
        sort_values('Predictions', ascending=False).dropna()
        top5_df = pd.DataFrame(movie_recs['Title'][:11])
        results = top5_df.to_dict('records')
        columnNames = top5_df.columns.values

        return render_template('recommendation.html', records = results, colnames = columnNames)






        # movies_map = data.copy()
        # movies_map.reset_index(inplace=True)
        # movies_map = movies_map.rename(columns={'index': 'id'})
        # movies = movies_map.iloc[movie_indices][['Title', 'id']]
        # new_ratings = pd.read_csv('new_ratings.csv')
        # reader = Reader()
        # Dataset.load_from_df(new_ratings[['userId', 'movieId', 'rating']], reader)
        # svd = joblib.load('svd.pkl')
        # movies['est'] = movies['id'].apply(lambda x: svd.predict(user, movies_map.loc[x]['movieId']).est)
        # movies = movies.sort_values('est', ascending=False)
        # top10_df = pd.DataFrame(movies['Title'][:11])
        # results = top10_df.to_dict('records')
        # columnNames = top10_df.columns.values
                
        # return render_template('recommendation.html', records = results, colnames = columnNames)


if __name__ == '__main__':
    app.run(debug=True)