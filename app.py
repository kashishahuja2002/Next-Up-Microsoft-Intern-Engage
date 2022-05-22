
import pickle
import numpy as np
import pandas as pd
import requests
import flask
import ast
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

dataset = pickle.load(open('./model/data/dataset.pkl', 'rb'))
movies = pd.DataFrame(dataset)

similarity = pickle.load(open('./model/data/similarity.pkl', 'rb'))
popular = pickle.load(open('./model/data/popular.pkl', 'rb'))
select = pickle.load(open('./model/data/select.pkl', 'rb'))

movie_names = movies['title'].values


def byChoice(genres, castList, obj):
    choice = obj.copy()

    def byChoiceGenre():
        gen_fre = []
        for row in choice.iterrows():
            genFre = 0
            for gen in row[1].genres:
                if gen == genres[0] or gen == genres[1] or gen == genres[2]:
                    genFre += 1
            gen_fre.append(genFre)
        return gen_fre

    choice['gen_fre'] = byChoiceGenre()
    choice = choice[choice['gen_fre'] != 0]

    def byChoiceCast():
        cast_fre = []
        for row in choice.iterrows():
            castFre = 0
            for cast in row[1].cast:
                if cast == castList[0] or cast == castList[1] or cast == castList[2] or cast == castList[3] or cast == \
                        castList[4] or cast == castList[5]:
                    castFre += 1
            cast_fre.append(castFre)
        return cast_fre

    choice['cast_fre'] = byChoiceCast()
    choice = choice[choice['cast_fre'] != 0]

    choice_movies = []
    counter = 0
    for mov in choice.iterrows():
        if counter != 3:
            choice_movies.append(mov[1].title)
            counter += 1
        else:
            break
    return choice_movies


def fetchTrailer(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}/videos?api_key=65669b357e1045d543ba072f7f533bce&language=en-US'.format(
            movie_id))
    data = response.json()
    for vid in data['results']:
        if vid['name'].find("Trailer") != -1:
            return vid['key']


def fetchPoster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=65669b357e1045d543ba072f7f533bce&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + str(data['poster_path'])


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
    movie_poster = fetchPoster(movie_id)

    return render_template("movie.html", movie_names=movie_names, movies=movies, movie_idx=movie_idx, recommendations=recommendations, posters=posters, trailer_key=trailer_key, movie_poster=movie_poster)


def byGenre(genre):
    counter = 0
    genre_movies = []
    for row in popular.iterrows():
        if counter != 6:
            for gen in row[1].genres:
                if gen == genre:
                    genre_movies.append(row[1].title)
                    counter += 1
                    break
        else:
            break

    genre_posters = []
    for i in genre_movies:
        movie_index = movies[movies['title'] == i].index[0]
        movie_id = movies.iloc[movie_index].movie_id
        genre_posters.append(fetchPoster(movie_id))

    return genre_movies, genre_posters


def byYear(year):
    counter = 0
    year_movies = []
    for row in popular.iterrows():
        if row[1].release_date == year:
            if counter != 6:
                year_movies.append(row[1].title)
                counter = counter + 1
            else:
                break

    year_posters = []
    for i in year_movies:
        movie_index = movies[movies['title'] == i].index[0]
        movie_id = movies.iloc[movie_index].movie_id
        year_posters.append(fetchPoster(movie_id))

    return year_movies, year_posters


@app.route('/getByGenre', methods=['GET','POST'])
def getByGenre():
    genre = request.form["genre"]
    genre_movies, genre_poster = byGenre(genre)
    response = jsonify(
        {"genre_movies": genre_movies}, {"genre_posters": genre_poster}
    )
    return response


@app.route('/getByYear', methods=['GET','POST'])
def getByYear():
    year = request.form["year"]
    year_movies, year_poster = byYear(year)
    response = jsonify(
        {"year_movies": year_movies}, {"year_posters": year_poster}
    )
    return response


@app.route('/recommendations')
def recommendations():
    genre_movies, genre_posters = byGenre("Action")
    year_movies, year_posters = byYear("2016")
    genres = ["Drama", "Documentory", "Horror"]
    castList = ["Sandra Bullock", "Jessica Chastain", "Ryan Reynolds", "Zoe Saldana", "Chris Pratt","Lisa Hart Carroll"]
    choice_movies = byChoice(genres,castList,select)
    choice_idx = []
    choice_posters=[]
    for mov in choice_movies:
        movie_idx = movies[movies['title'] == mov].index[0]
        choice_idx.append(movie_idx)
        movie_id = movies.iloc[movie_idx].movie_id
        choice_posters.append(fetchPoster(movie_id))
    return render_template("recommendations.html", movie_names=movie_names, genre_movies=genre_movies, year_movies=year_movies, genre_posters=genre_posters, year_posters=year_posters, choice_idx=choice_idx, movies=movies, choice_posters=choice_posters)


if __name__ == "__main__":
    app.run()


# movie_ids = movies['movie_id'].values
# for x in range(1, 100):
#     movie_id = movies.iloc[x].movie_id
#     print(fetchPoster(movie_id))

    # for i in movie_ids:
    #     print(fetchPoster(i))



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



