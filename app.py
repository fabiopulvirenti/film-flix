from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap5

from database_ops import retrieve_all_movies, retrieve_one_movie, insert_movie, delete_record, update_record, \
     retrieve_one_movie_by_title

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/films/", methods=["GET"])
def get_all_films_page():
    list_movies = retrieve_all_movies()

    return render_template('list.html', movies=list_movies)



@app.route("/create", methods=["GET"])
def add_movie_page():
    return render_template("add_movie.html")

@app.route("/create", methods=["POST"])
def add_movie():
    title=request.form['title']
    yearReleased = int(request.form['year'])
    rating = request.form['rating']
    duration = int(request.form['duration'])
    genre =  request.form['genre']

    # print(title)
    insert_movie(title,yearReleased,rating,duration,genre)

    return redirect(url_for('get_all_films_page'))


@app.route("/films/<int:film_id>/edit", methods=["GET"])
def modify_movie_page(film_id):
    movie_selected = retrieve_one_movie(film_id)

    return render_template('modify_movie.html', movie=movie_selected)

@app.route("/films/search", methods=["POST"])
def give_me_the_movie_by_title():
    search_string = request.form['search_string']
    title_selected=retrieve_one_movie_by_title(search_string)

    return render_template('title_selected.html',movies=title_selected)
    # return redirect(url_for('get_all_films_page'))



@app.route("/films/<int:film_id>/edit", methods=["POST"])
def modify_movie(film_id):
    title = request.form['title']
    yearReleased = int(request.form['year'])
    rating = request.form['rating']
    duration = int(request.form['duration'])
    genre = request.form['genre']

    update_record(title,yearReleased,rating,duration,genre,film_id)

    return redirect(url_for("get_one_film_by_id_page",film_id=film_id))



@app.route("/films/<int:film_id>", methods=["POST"])
def delete_movie(film_id):
    delete_record(film_id)

    return redirect(url_for('get_all_films_page'))





@app.route("/films/<int:film_id>", methods=["GET"])
def get_one_film_by_id_page(film_id):
    movie_selected = retrieve_one_movie(film_id)

    return render_template('movie.html', movie=movie_selected)

@app.route("/about",methods=["GET"])
def about_page():
    return render_template('about.html')


@app.route("/api/films/", methods=["GET"])
def get_all_films():
    list_movies = retrieve_all_movies()

    return list_movies


@app.route("/api/films/<int:film_id>", methods=["GET"])
def get_one_record(film_id):
    movie = retrieve_one_movie(film_id)

    return movie


if __name__ == '__main__':
    app.run(port=8080, debug=True)
