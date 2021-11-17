from flask import make_response, abort
from config import db
from models import Directors, DirectorSchema


def read_all():
    """
    This function responds to a request for /api/director
    with the complete lists of director
    :return:        json string of list of director
    """
    director = Directors.query.order_by(db.desc(Directors.id)).limit(20)

    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data


def read_one(director_id):
    """
    This function responds to a request for /api/director/{director_id}
    with one matching director from directors
    :param director_id:   Id of direcotr to find
    :return:            director matching id
    """
    director = Directors.query.filter(Directors.id == director_id).one_or_none()

    if director is not None:

        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data

    else:
        abort(
            404,
            "Director not found for Id: {director_id}".format(director_id=director_id),
        )


def create(director):
    """
    This function creates a new director in the directors structure
    based on the passed in director data
    :param director:  director to create in directors structure
    :return:        201 on success, 406 on director exists
    """
    uid = director.get("uid")
    name = director.get("name")
    existing_director = (
        Directors.query.filter(Directors.uid == uid)
        .filter(Directors.name == name)
        .one_or_none()
    )

    if existing_director is None:

        schema = DirectorSchema()
        new_director = schema.load(director, session=db.session)

        db.session.add(new_director)
        db.session.commit()

        data = schema.dump(new_director)

        return data, 201

    else:
        abort(
            409,
            "Director with {name} and {uid} already exists".format(
                name=name, uid=uid
            ),
        )


def update(director_id, director):
    """
    This function updates an existing director in the directors structure
    Throws an error if a director with the name and uid we want to update to
    already exists in the database.
    :param director_id:   Id of the director to update in the directors structure
    :param director:      director to update
    :return:            updated director structure
    """
    update_director = Directors.query.filter(
        Directors.id == director_id
    ).one_or_none()

    name = director.get("name")
    uid = director.get("uid")

    existing_director = (
        Directors.query.filter(Directors.name == name)
        .filter(Directors.uid == uid)
        .one_or_none()
    )

    if update_director is None:
        abort(
            404,
            "Director not found for Id: {director_id}".format(director_id=director_id),
        )

    elif (
        existing_director is not None and existing_director.id != director_id
    ):
        abort(
            409,
            "Director {name} with {uid} already exists".format(
                name=name, uid=uid
            ),
        )

    else:

        schema = DirectorSchema()
        update = schema.load(director, session=db.session)
        update.id = update_director.id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_director)

        return data, 200


def delete(director_id):
    """
    This function deletes a director from the people structure
    :param director_id:   Id of the director to delete
    :return:            200 on successful delete, 404 if not found
    """
    director = Directors.query.filter(Directors.id == director_id).one_or_none()

    if director_id is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(
            "Director {director_id} deleted".format(director_id=director_id), 200
        )

    else:
        abort(
            404,
            "Director not found for Id: {director_id}".format(director_id=director_id),
        )
        
def read_one_revenue(director_id):
    """
    This function responds to a request for /api/director/revenue/{director_id}
    with one matching director from directors
    :param director_id:   Id of director to find
    :return:            director matching id
    """
    director = Directors.query.filter(Directors.id == director_id).one_or_none()

    if director is not None:
        total_rev = 0
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        # print("Ini pendapatan")
        for movie_data in data["movies"] :
            total_rev+=movie_data["revenue"]
        return total_rev

    else:
        abort(
            404,
            "Director not found for Id: {director_id}".format(director_id=director_id),
        )
        
def read_one_voting_average(director_id):
    """
    This function responds to a request for /api/director/votingaverage/{director_id}
    with one matching director from directors
    :param director_id:   Id of direcotr to find
    :return:            director matching id
    """
    director = Directors.query.filter(Directors.id == director_id).one_or_none()

    if director is not None:
        total_voting = 0
        i = 0
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        # print("Ini pendapatan")
        for movie_data in data["movies"] :
            i+=1
            total_voting+=movie_data["vote_average"]
            
        total_voting = total_voting/i
        return total_voting

    else:
        abort(
            404,
            "Director not found for Id: {director_id}".format(director_id=director_id),
        )

def read_one_profit(director_id):
    """
    This function responds to a request for /api/director/votingaverage/{director_id}
    with one matching director from directors
    :param director_id:   Id of direcotr to find
    :return:            director matching id
    """
    director = Directors.query.filter(Directors.id == director_id).one_or_none()

    if director is not None:
        total_budget = 0
        total_profit = 0
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        # print("Ini pendapatan")
        for movie_data in data["movies"] :
            total_budget+=movie_data["budget"]
            total_profit+=movie_data["revenue"]
            
        total_profit = total_profit - total_budget
        return total_profit

    else:
        abort(
            404,
            "Director not found for Id: {director_id}".format(director_id=director_id),
        )