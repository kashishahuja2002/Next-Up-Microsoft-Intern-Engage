
import pickle
import numpy as np
import pandas as pd
import requests
import flask
import ast
from flask import Flask, redirect, render_template, request, jsonify, url_for
from flask_cors import CORS, cross_origin
import operator
import sqlite3

app = Flask(__name__)


def db_connection():
    conn=None
    try:
        conn = sqlite3.connect('users.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn


dataset = pickle.load(open('./model/data/dataset.pkl', 'rb'))
movies = pd.DataFrame(dataset)

similarity = pickle.load(open('./model/data/similarity.pkl', 'rb'))
popular = pickle.load(open('./model/data/popular.pkl', 'rb'))
select = pickle.load(open('./model/data/select.pkl', 'rb'))


@app.route('/')
def index():
    return render_template("index.html")


signup_email  = ""
signup_password  = ""
signup_mobile  = ""
@app.route('/signup', methods=['GET','POST'])
def signup():
    global signup_email
    global signup_password
    global signup_mobile
    response = render_template("signup.html")

    if request.method == 'POST':
        conn = db_connection()
        cursor = conn.cursor()

        signup_email = request.form["email"]
        signup_mobile = request.form["mobile"]
        signup_password = request.form["password"]

        sql_query = "Select email from users where email= '"+signup_email+"'"
        cursor.execute(sql_query)
        results = cursor.fetchall()

        if len(results) != 0:
            response = "This email is already registered. <br> Please sign-in."
        else:
            response = "choices"
    return response


signin_email = ""
@app.route('/signin', methods=['GET','POST'])
def signin():
    global signin_email
    response = render_template("signin.html")

    if request.method == 'POST':
        conn = db_connection()
        cursor = conn.cursor()

        signin_email = request.form["email"]
        password = request.form["password"]

        sql_query = "Select email, password from users where email= '"+signin_email+"'"
        cursor.execute(sql_query)
        results = cursor.fetchall()

        if len(results) == 0:
            response = "This email is not registered. <br> Please sign-up first."
        elif password != results[0][1]:
                response = "Incorrect Password."
        elif password == results[0][1]:
            response = "recommendations"

    return response


@app.route('/choices', methods=['GET','POST'])
def choices():

    genre_names = []
    for i in movies['genres']:
        for gen in i:
            if gen not in genre_names:
                genre_names.append(gen)

    cast_dict = {}
    for row in movies.iterrows():
        for cast in row[1].cast:
            if cast in cast_dict:
                cast_dict[cast] = (cast_dict[cast] + 1)
            else:
                cast_dict[cast] = 0
    cast_dict = dict(sorted(cast_dict.items(), key=operator.itemgetter(1), reverse=True))
    cast_names = []
    counter = 0
    for key in cast_dict:
        if counter < 25:
            cast_names.append(key)
            counter += 1
        else:
            break

    return render_template("choices.html", genre_names=genre_names, cast_names=cast_names)


movie_names = movies['title'].values

def fetchTrailer(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}/videos?api_key=65669b357e1045d543ba072f7f533bce&language=en-US'.format(
            movie_id))
    data = response.json()
    for vid in data['results']:
        if vid['name'].find("Trailer") != -1:
            return vid['key']


def fetchPoster(movie_id):
    movie_index = movies[movies['movie_id'] == movie_id].index[0]
    poster = movies.iloc[movie_index].poster_path
    return poster


def byChoice(genres, castList, obj):
    choice = obj.copy()

    def byChoiceCast():
        cast_fre = []
        for row in choice.iterrows():
            castFre = 0
            for cast in row[1].cast:
                for item in castList:
                    if cast == item:
                        castFre += 1
            cast_fre.append(castFre)
        return cast_fre

    choice['cast_fre'] = byChoiceCast()
    choice = choice[choice['cast_fre'] != 0]

    def byChoiceGenre():
        gen_fre = []
        for row in choice.iterrows():
            genFre = 0
            for gen in row[1].genres:
                for item in genres:
                    if gen == item:
                        genFre += 1
            gen_fre.append(genFre)
        return gen_fre

    choice['gen_fre'] = byChoiceGenre()
    choice = choice[choice['gen_fre'] != 0]

    choice = choice.sort_values('cast_fre', ascending=False)

    choice_movies = []
    counter = 0
    for mov in choice.iterrows():
        if counter != 3:
            choice_movies.append(mov[1].title)
            counter += 1
        else:
            break
    return choice_movies


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

@app.route('/getByGenre', methods=['GET','POST'])
def getByGenre():
    genre = request.form["genre"]
    genre_movies, genre_posters = byGenre(genre)
    response = jsonify(
        {"genre_movies": genre_movies}, {"genre_posters": genre_posters}
    )
    return response


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

@app.route('/getByYear', methods=['GET','POST'])
def getByYear():
    year = request.form["year"]
    year_movies, year_posters = byYear(year)
    response = jsonify(
        {"year_movies": year_movies}, {"year_posters": year_posters}
    )
    return response


@app.route('/recommendations', methods=['POST', 'GET'])
def recommendations():
    conn = db_connection()
    cursor = conn.cursor()
    selected_genres = []
    selected_cast = []

    if request.method == 'POST':
        genreList = request.form.getlist('genre-checkbox')
        castList = request.form.getlist('cast-checkbox')
        for i in genreList:
            selected_genres.append(i.replace("-", " "))
        for i in castList:
            selected_cast.append(i.replace("-", " "))

        # insert into database on signup
        global signup_email
        global signup_password
        global signup_mobile
        sg = ("$".join(selected_genres))
        sc = ("$".join(selected_cast))
        
        sql_query = """ Insert into users(email, password, mobile, selected_genres, selected_cast) values(?,?,?,?,?) """
        cursor.execute(sql_query, (signup_email, signup_password, signup_mobile, sg, sc))
        conn.commit()
        print(cursor.lastrowid)

    else:
        sql_query = " Select selected_genres, selected_cast from users where email= '"+signin_email+"'"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        selected_genres = list(results[0][0].split("$"))
        selected_cast = list(results[0][1].split("$")) 

    choice_movies = byChoice(selected_genres, selected_cast, select)
    choice_idx = []
    choice_posters = []
    for mov in choice_movies:
        movie_idx = movies[movies['title'] == mov].index[0]
        choice_idx.append(movie_idx)
        movie_id = movies.iloc[movie_idx].movie_id
        choice_posters.append(fetchPoster(movie_id))
    genre_movies, genre_posters = byGenre("Action")
    year_movies, year_posters = byYear("2016")

    return render_template("recommendations.html", movie_names=movie_names, genre_movies=genre_movies, year_movies=year_movies, genre_posters=genre_posters, year_posters=year_posters, choice_idx=choice_idx, movies=movies, choice_posters=choice_posters)


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


if __name__ == "__main__":
    app.run()

# movie_ids = movies['movie_id'].values
# for x in range(1, 100):
#     movie_id = movies.iloc[x].movie_id
#     print(fetchPoster(movie_id))

    # for i in movie_ids:
    #     print(fetchPoster(i))


# s = ['Geeks for geeks', 'for alla', 'Geeks djfh jhsds']
# new="$".join(s)
# print(new)
#
# ano=list(new.split("$"))
# print(ano)

# // $('input[name="genres"]:checked').each(function() {
# //     console.log(this.value);
# // });


