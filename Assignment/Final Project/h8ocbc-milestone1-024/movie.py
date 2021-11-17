"""
This is the movie module and supports all the REST actions for the
movie data
"""

from flask import make_response, abort
from config import db
from models import Directors, Movies, MovieSchema


def read_all():
    """
    This function responds to a request for /api/movie
    with the complete list of movies, sorted by movie id

    :return:                json list of all movies for all people
    """
    movies = Movies.query.order_by(db.desc(Movies.id)).limit(20)
    
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    
    return data


def read_one(movie_id):
    """
    This function responds to a request for
    /api/movie/{movie_id}
    with one matching movie for the associated director

    :param movie_id:       Id of movie
    :return:                json string of movie contents
    """
    movie = (
        Movies.query.join(Directors, Directors.id == Movies.director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )

    if movie is not None:
        movie_schema = MovieSchema()
        data = movie_schema.dump(movie)
        return data

    else:
        abort(404, f"Movie not found for Id: {movie_id}")


def create(director_id, movie):
    """
    This function creates a new movie related to the passed in director id.

    :param director_id:       Id of the director the movie is related to
    :param movie:            The JSON containing the movie data
    :return:                201 on success
    """
    director = Directors.query.filter(Directors.id == director_id).one_or_none()

    if director is None:
        abort(404, f"Director not found for Id: {director_id}")

    schema = MovieSchema()
    new_movie = schema.load(movie, session=db.session)

    director.movies.append(new_movie)
    db.session.commit()

    data = schema.dump(new_movie)

    return data, 201


def update(movie_id, movie):
    """
    This function updates an existing movie

    :param movie_id:         Id of the movie to update
    :param movie:            The JSON containing the movie data
    :return:                200 on success
    """
    update_movie = (
        Movies.query.join(Directors, Directors.id == Movies.director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )

    if update_movie is not None:

        schema = MovieSchema()
        update = schema.load(movie, session=db.session)

        update.director_id = update_movie.director_id
        update.id = update_movie.id
        
        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_movie)

        return data, 200

    else:
        abort(404, f"Movie not found for Id: {movie_id}")


def delete(movie_id):
    """
    This function deletes a movie from the movie structure
    
    :param movie_id:     Id of the movie to delete
    :return:            200 on successful delete, 404 if not found
    """
    movie = (
        Movies.query.filter(Movies.id == movie_id)
        .one_or_none()
    )

    if movie is not None:
        db.session.delete(movie)
        db.session.commit()
        return make_response(
            "Movie {movie_id} deleted".format(movie_id=movie_id), 200
        )

    else:
        abort(404, f"Movie not found for Id: {movie_id}")

def read_top_voting():
    """
    This function responds to a request for /api/movie/topvoting
    with the complete list of movies, sorted by movie id

    :return:                json list of all movies for all people
    """
    movies = Movies.query.order_by(db.desc(Movies.vote_average)).limit(5)
    
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    
    return data

def read_top_revenue():
    """
    This function responds to a request for /api/movie
    with the complete list of movies, sorted by movie id

    :return:                json list of all movies for all people
    """
    movies = Movies.query.order_by(db.desc(Movies.revenue)).limit(5)
    
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    
    return data