FETCH_ALL_MOVIES = "Select * from movies"
INSERT_USER = "Insert into users(email, password, mobile, selected_genres, selected_cast) values(?,?,?,?,?)"
FETCH_ALL_CHOICE = "Select * from choice"
SORT_BY_CAST = "Select title from choice where (genFre>0 AND castFre >0) order by castFre DESC"
FETCH_GENRES_POPULAR = "Select movie_id, genres from popular"
FETCH_DATE_POPULAR = "Select movie_id, release_date from popular"

