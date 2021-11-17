from flask import make_response, abort
from config import db
from models import Person, PersonSchema


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    people = Person.query.order_by(Person.person_id).all()

    person_schema = PersonSchema(many=True)
    data = person_schema.dump(people)
    return data


def read_one(person_id):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people
    :param person_id:   Id of person to find
    :return:            person matching id
    """
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person is not None:

        person_schema = PersonSchema()
        data = person_schema.dump(person)
        return data

    else:
        abort(
            404,
            "Person not found for Id: {person_id}".format(person_id=person_id),
        )


def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    fname = person.get("fname")
    lname = person.get("lname")

    existing_person = (
        Person.query.filter(Person.fname == fname)
        .filter(Person.lname == lname)
        .one_or_none()
    )

    if existing_person is None:

        schema = PersonSchema()
        new_person = schema.load(person, session=db.session)

        db.session.add(new_person)
        db.session.commit()

        data = schema.dump(new_person)

        return data, 201

    else:
        abort(
            409,
            "Person {fname} {lname} exists already".format(
                fname=fname, lname=lname
            ),
        )


def update(person_id, person):
    """
    This function updates an existing person in the people structure
    Throws an error if a person with the name we want to update to
    already exists in the database.
    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    update_person = Person.query.filter(
        Person.person_id == person_id
    ).one_or_none()

    fname = person.get("fname")
    lname = person.get("lname")

    existing_person = (
        Person.query.filter(Person.fname == fname)
        .filter(Person.lname == lname)
        .one_or_none()
    )

    if update_person is None:
        abort(
            404,
            "Person not found for Id: {person_id}".format(person_id=person_id),
        )

    elif (
        existing_person is not None and existing_person.person_id != person_id
    ):
        abort(
            409,
            "Person {fname} {lname} exists already".format(
                fname=fname, lname=lname
            ),
        )

    else:

        schema = PersonSchema()
        update = schema.load(person, session=db.session)

        update.person_id = update_person.person_id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_person)

        return data, 200


def delete(person_id):
    """
    This function deletes a person from the people structure
    :param person_id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person is not None:
        db.session.delete(person)
        db.session.commit()
        return make_response(
            "Person {person_id} deleted".format(person_id=person_id), 200
        )

    else:
        abort(
            404,
            "Person not found for Id: {person_id}".format(person_id=person_id),
        )