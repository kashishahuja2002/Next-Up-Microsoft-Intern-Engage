
import json
import pickle
import numpy as np
import pandas as pd
import requests
import flask
import ast
from flask import Flask, render_template
# from flask_cors import CORS, cross_origin

app = Flask(__name__)

dataset = pickle.load(open('dataset.pkl', 'rb'))
movies = pd.DataFrame(dataset)

similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_names = movies['title'].values


def fetchTrailer(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}/videos?api_key=65669b357e1045d543ba072f7f533bce&language=en-US'.format(
            movie_id))
    data = response.json()
    print(data)
    for vid in data['results']:
        if (vid['name'] == "Official Trailer"):
            return vid['key']


def fetchPoster(movie_id):
    print(movie_id)
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=65669b357e1045d543ba072f7f533bce&language=en-US'.format(
            movie_id))
    data = response.json()
    print(str(data['poster_path']))
    return "https://image.tmdb.org/t/p/w185/" + str(data['poster_path'])

@app.route('/movie/<movie_name>')
def movie(movie_name):

    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

        recommended_movies = []
        movie_posters = []
        for i in movies_list:
            rec_movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            movie_posters.append(fetchPoster(rec_movie_id))
        return recommended_movies, movie_posters

    selected_movie = movie_name
    movie_idx = movies[movies['title'] == selected_movie].index[0]
    movie_id = movies.iloc[movie_idx].movie_id
    recommendations, posters = recommend(selected_movie)
    trailer_key = fetchTrailer(movie_id)

    return render_template("movie.html", movie_names=movie_names, movies=movies, movie_idx=movie_idx, recommendations=recommendations, posters=posters, trailer_key=trailer_key)

@app.route('/recommendations')
def recommendations():
    def byYear(year):
        counter = 0
        L = []
        for row in movies.iterrows():
            if row[1].release_date == year:
                if counter != 6:
                    L.append(row[1].title)
                    counter = counter + 1
                else:
                    break
        return L

    def byGenre(genre):
        counter = 0
        L = []
        for row in movies.iterrows():
            if counter != 6:
                for gen in row[1].genres:
                    if gen == genre:
                        L.append(row[1].title)
                        counter += 1
                        break
            else:
                break
        return L

    genre_movies = byGenre("Comedy")
    year_movies = byYear("2016")

    genre_posters = []
    for i in genre_movies:
        movie_index = movies[movies['title'] == i].index[0]
        movie_id = movies.iloc[movie_index].movie_id
        genre_posters.append(fetchPoster(movie_id))

    year_posters = []
    for i in year_movies:
        movie_index = movies[movies['title'] == i].index[0]
        movie_id = movies.iloc[movie_index].movie_id
        year_posters.append(fetchPoster(movie_id))

    return render_template("recommendations.html", movie_names=movie_names, genre_movies=genre_movies, year_movies=year_movies, genre_posters=genre_posters, year_posters=year_posters)

if __name__ == "__main__":
    app.run()




# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
#
#     recommended_movies = []
#     for i in movies_list:
#         print(i)
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies
#
# dataset = pickle.load(open('dataset.pkl','rb'))
# movies = pd.DataFrame(dataset)
#
# similarity = pickle.load(open('similarity.pkl','rb'))
#
# selected_movie = "Avatar"
# recommendations = recommend(selected_movie)
# for i in posters:
#     print(i)

# movie_index = movies[movies['title'] == selected_movie].index[0]
# print(movies.iloc[movie_index].title)
# print(movies.iloc[movie_index].overview)



