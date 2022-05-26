import pickle
import pandas as pd
import requests
from flask import Flask, redirect, render_template, request, jsonify, url_for, session
import operator
import sqlite3
from annoy import AnnoyIndex
from flask_mail import Mail, Message
from random import randint

app = Flask(__name__)
app.secret_key = "secret key"

# Flask mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "kashishahuja2002@gmail.com"
app.config['MAIL_PASSWORD'] = "dleiatmoyykkaafn"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# Database connections
# users table
def db_user_connection():
    conn = None
    try:
        conn = sqlite3.connect('./model/data/users.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

# popular table
def db_popular_connection():
    conn = None
    try:
        conn = sqlite3.connect('./model/data/popular.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

# choice table
def db_choice_connection():
    conn = None
    try:
        conn = sqlite3.connect('./model/data/choice.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

# movies table
def db_movies_connection():
    conn = None
    try:
        conn = sqlite3.connect('./model/data/movies.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

conn = db_movies_connection()
cursor = conn.cursor()
sql_query = "Select * from movies"
cursor.execute(sql_query)
movies_result = cursor.fetchall()


# Home page
@app.route('/')
def index():
    return render_template("index.html")


# Signup page
signup_email = ""
signup_password = ""
signup_mobile = ""
@app.route('/signup', methods=['GET','POST'])
def signup():
    global signup_email
    global signup_password
    global signup_mobile
    response = render_template("signup.html")

    if request.method == 'POST':
        conn = db_user_connection()
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
            session["user"] = signup_email
            response = "choices"
    return response


# Signin page
signin_email = ""
@app.route('/signin', methods=['GET','POST'])
def signin():
    global signin_email
    response = render_template("signin.html")

    if request.method == 'POST':
        conn = db_user_connection()
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
            session["user"] = signin_email
            response = "recommendations"

    return response


# Choices page
@app.route('/choices', methods=['GET','POST'])
def choices():
    global signup_email
    global movies_result
    if "user" in session and session["user"] == signup_email:

        genre_names = []
        cast_dict = {}
        for row in movies_result:
            mov_gen = list(row[5].split("$"))
            for gen in mov_gen:
                if gen not in genre_names and gen != '':
                    genre_names.append(gen)

            mov_cast = list(row[7].split("$"))
            for cast in mov_cast:
                if cast in cast_dict and cast != '':
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
    else:
        print("Session not found")
        return redirect(url_for("signup"))


movie_names = []
for row in movies_result:
    movie_names.append(row[2])

def fetchTrailer(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}/videos?api_key=65669b357e1045d543ba072f7f533bce&language=en-US'.format(
            movie_id))
    data = response.json()
    for vid in data['results']:
        if vid['name'].find("Trailer") != -1:
            return vid['key']

def fetchBackdrop(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=65669b357e1045d543ba072f7f533bce&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original"+str(data['backdrop_path'])


def fetchPoster(movie_id):
    for row in movies_result:
        if row[1] == movie_id:
            movie_index = row[0]
            break;
    poster = movies_result[movie_index][11]
    return poster


def byChoice(genreList, castList):

    conn = db_choice_connection()
    cursor = conn.cursor()
    sql_query = "Select * from choice"
    cursor.execute(sql_query)
    results = cursor.fetchall()

    for row in results:
        cf = 0
        mov_cast = list(row[4].split("$"))
        for cast in mov_cast:
            for c in castList:
                if cast == c:
                    cf += 1
        if cf != 0:
            sql_query = "Update choice set castFre = " + str(cf)+" where movie_id = "+str(row[1])
            cursor.execute(sql_query)

    for row in results:
        gf = 0
        mov_gen = list(row[3].split("$"))
        for gen in mov_gen:
            for g in genreList:
                if gen == g:
                    gf += 1
        if gf != 0:
            sql_query = "Update choice set genFre = "+str(gf)+" where movie_id = "+str(row[1])
            cursor.execute(sql_query)

    sql_query = "Select title from choice where (genFre>0 AND castFre >0) order by castFre DESC"
    cursor.execute(sql_query)
    results = cursor.fetchall()

    choice_movies = []
    counter = 0
    for row in results:
        if counter != 3:
            choice_movies.append(row[0])
            counter += 1
        else:
            break
    return choice_movies


def byGenre(genre):
    counter = 0
    genre_movies = []
    genre_posters = []

    conn = db_popular_connection()
    cursor = conn.cursor()
    sql_query = "Select movie_id, genres from popular"
    cursor.execute(sql_query)
    results = cursor.fetchall()

    for row in results:
        if counter != 6:
            mov_gen = list(row[1].split("$"))
            for gen in mov_gen:
                if gen == genre:
                    cursor.execute("Select title from popular where movie_id = '"+str(row[0])+"'")
                    title = cursor.fetchall()
                    genre_movies.append(title[0][0])
                    genre_posters.append(fetchPoster(row[0]))
                    counter += 1
                    break
        else:
            break

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
    year_posters = []

    conn = db_popular_connection()
    cursor = conn.cursor()
    sql_query = "Select movie_id, release_date from popular"
    cursor.execute(sql_query)
    results = cursor.fetchall()

    for row in results:
        if counter != 6:
            if year == row[1]:
                cursor.execute("Select title from popular where movie_id = '"+str(row[0])+"'")
                title = cursor.fetchall()
                year_movies.append(title[0][0])
                year_posters.append(fetchPoster(row[0]))
                counter += 1
        else:
            break

    return year_movies, year_posters

@app.route('/getByYear', methods=['GET','POST'])
def getByYear():
    year = request.form["year"]
    year_movies, year_posters = byYear(year)
    response = jsonify(
        {"year_movies": year_movies}, {"year_posters": year_posters}
    )
    return response


# Recommendations page
@app.route('/recommendations', methods=['POST', 'GET'])
def recommendations():
    global signin_email
    global signup_email

    conn = db_user_connection()
    cursor = conn.cursor()
    selected_genres = []
    selected_cast = []

    # sign-up
    if request.method == 'POST':
        genreList = request.form.getlist('genre-checkbox')
        castList = request.form.getlist('cast-checkbox')
        for i in genreList:
            selected_genres.append(i.replace("-", " "))
        for i in castList:
            selected_cast.append(i.replace("-", " "))

        # insert into database on signup
        sg = ("$".join(selected_genres))
        sc = ("$".join(selected_cast))
        global signup_password
        global signup_mobile

        sql_query = """ Insert into users(email, password, mobile, selected_genres, selected_cast) values(?,?,?,?,?) """
        cursor.execute(sql_query, (signup_email, signup_password, signup_mobile, sg, sc))
        conn.commit()
        print(cursor.lastrowid)

    # sign-in
    else:
        sql_query = " Select selected_genres, selected_cast from users where email= '"+session["user"]+"'"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        selected_genres = list(results[0][0].split("$"))
        selected_cast = list(results[0][1].split("$"))

    if "user" in session:
        choice_movies = byChoice(selected_genres, selected_cast)
        choice_idx = []
        choice_posters = []
        for mov in choice_movies:
            for row in movies_result:
                if row[2] == mov:
                    movie_idx = row[0]
                    movie_id = row[1]
                    break;
            choice_idx.append(movie_idx)
            choice_posters.append(fetchBackdrop(movie_id))
        genre_movies, genre_posters = byGenre("Action")
        year_movies, year_posters = byYear("2016")

        return render_template("recommendations.html", movie_names=movie_names, genre_movies=genre_movies, year_movies=year_movies, genre_posters=genre_posters, year_posters=year_posters, choice_idx=choice_idx, movies_result=movies_result, choice_posters=choice_posters)
    else:
        print("Session not found")
        return redirect(url_for("signin"))


# Movie page
@app.route('/movie/<movie_name>')
def movie(movie_name):

    if "user" in session:
        def recommend(movie):
            for row in movies_result:
                if row[2] == movie:
                    movie_index = row[0]
                    break;
            u = AnnoyIndex(5000, 'angular')
            u.load('./model/data/vectors.ann')
            movies_list = (u.get_nns_by_item(movie_index, 7))[1:7]  # returns index of 6 similar movies

            recommended_movies = []
            movie_posters = []
            for i in movies_list:
                rec_movie_id = movies_result[i][1]
                recommended_movies.append(movies_result[i][2])
                movie_posters.append(fetchPoster(rec_movie_id))
            return recommended_movies, movie_posters

        selected_movie = movie_name
        for row in movies_result:
            if row[2] == selected_movie:
                movie_idx = row[0]
                movie_id = row[1]
                break;
        recommendations, posters = recommend(selected_movie)
        trailer_key = fetchTrailer(movie_id)
        movie_poster = fetchPoster(movie_id)

        mov_genre = []
        mov_cast = []
        for row in movies_result:
            mg = list(row[5].split("$"))
            mov_genre.append(mg)
            mc = list(row[7].split("$"))
            mov_cast.append(mc)

        return render_template("movie.html", movie_names=movie_names, movies_result=movies_result, movie_idx=movie_idx, recommendations=recommendations, posters=posters, trailer_key=trailer_key, movie_poster=movie_poster, mov_genre=mov_genre, mov_cast=mov_cast)
    else:
        print("Session not found")
        return redirect(url_for("signin"))


# Watch page
@app.route('/watch/<movie_name>')
def watch(movie_name):
    if "user" in session:
        return render_template("watch.html", movie_name=movie_name)
    else:
        print("Session not found")
        return redirect(url_for("signin"))



otp = ""
# Forgot page
@app.route('/forgot', methods=['POST', 'GET'])
def forgot():
    global signin_email
    global otp

    response = render_template("forgotPass.html")
    if request.method == 'POST':
        conn = db_user_connection()
        cursor = conn.cursor()

        signin_email = request.form["email"]

        sql_query = "Select email, password from users where email= '"+signin_email+"'"
        cursor.execute(sql_query)
        results = cursor.fetchall()

        if len(results) == 0:
            response = "This email is not registered. <br> Please sign-up first."
        else:
            response = "forgot"

    if response == "forgot":
        range_start = 10**(6-1)
        range_end = (10**6)-1
        otp = randint(range_start, range_end)
        message = Message("NEW3 OTP for password reset", sender="kashishahuja2002@gmail.com", recipients=[signin_email])
        message.body = "OTP: "+str(otp)
        mail.send(message)

    return response


# reset page
@app.route('/reset', methods=['GET','POST'])
def reset():
    global otp
    response = render_template("reset.html")
    if request.method == 'POST':
        num = request.form["otp"]
        if str(num) == str(otp):
            response = "valid"
        else:
            response = "OTP entered is incorrect"

    return response


# change password in database
@app.route('/change', methods=['GET','POST'])
def change():
    global signin_email
    if request.method == 'POST':
        newPass = request.form["newPass"]
        conn = db_user_connection()
        cursor = conn.cursor()
        sql_query = "Update users set password = '"+newPass+"' where email = '"+signin_email+"'"
        cursor.execute(sql_query)
        conn.commit()
        session["user"] = signin_email

    return "recommendations"


# Logout
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)


