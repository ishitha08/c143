from flask import Flask,jsonify,request
import csv
from demographicFiltering import output
from contentFiltering import getRecommendation

allmovies = []
with open('movies.csv')as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]

liked_movies = []
did_not_watched = []
unliked_movies = []

app = Flask(__name__)
@app.route("/get-movies")
def get_movie():
    return jsonify({
        "data":allmovies[0],
        "status":"success"
    })
@app.route("/liked_movies",methods = ["POST"])
def likedmovies():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"

    }),201

@app.route("/unliked_movies",methods = ["POST"])
def unlikedmovies():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    unliked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did_not_watched",methods = ["POST"])
def didNotWatched():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    did_not_watched.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/popular_movies")
def popular_movies():
    movie_data = []
    for movie in output:
        d = {"title":movie[0],"poster_link":movie[1],"release_date":movie[2],"vote_average":movie[3],"rating":movie[4],"overview":movie[5]}
        movie_data.append(d)
    return jsonify({"data":movie_data,"status":"success"}),201

@app.route("/recommended_movies")
def recommended_movies():
    recommendedMovies = []
    for likedMovies in liked_movies:
        output = getRecommendation(likedMovies[19])
        for data in output:
            recommendedMovies.append(data)
    import itertools
    recommendedMovies.sort()
    recommendedMovies = list(recommendedMovies for recommendedMovies,_ in itertools.groupby(recommendedMovies))
    movie_data = []
    for recommended in recommendedMovies:
        d = {"title":recommended[0],"poster_link":recommended[1],"release_date":recommended[2],"vote_average":recommended[3],"rating":recommended[4],"overview":recommended[5]}
        movie_data.append(d)
    return jsonify({"data":movie_data,"status":"success"}),200


if __name__ == "__main__":
    app.run()
