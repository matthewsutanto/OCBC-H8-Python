from flask import make_response, abort
from config import db
from models import AvoType, AvoTypeSchema


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    avotype = AvoType.query.order_by(AvoType.typeid).all()

    avotype_schema = AvoTypeSchema(many=True)
    data = avotype_schema.dump(avotype)
    return data


def read_one(avotype_id):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people
    :param person_id:   Id of person to find
    :return:            person matching id
    """
    avotype = AvoType.query.filter(AvoType.typeid == avotype_id).one_or_none()

    if avotype is not None:

        avoType_schema = AvoTypeSchema()
        data = avoType_schema.dump(avotype)
        return data

    else:
        abort(
            404,
            "Person not found for Id: {avotype_id}".format(avotype_id=avotype_id),
        )


def create(avotype):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    type = avotype.get("type")

    existing_avotype = (
        AvoType.query.filter(AvoType.type == type)
        .one_or_none()
    )

    if existing_avotype is None:

        schema = AvoTypeSchema()
        new_avotype = schema.load(avotype, session=db.session)

        db.session.add(new_avotype)
        db.session.commit()

        data = schema.dump(new_avotype)

        return data, 201

    else:
        abort(
            409,
            "Avocado type {type} exists already".format(type=type),
        )


def update(avotype_id, avotype):
    """
    This function updates an existing person in the people structure
    Throws an error if a person with the name we want to update to
    already exists in the database.
    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    update_avotype = AvoType.query.filter(
        AvoType.typeid == avotype_id
    ).one_or_none()

    type = avotype.get("type")

    existing_avotype = (
        AvoType.query.filter(AvoType.type == type)
        .one_or_none()
    )

    if update_avotype is None:
        abort(
            404,
            "Avocado Type not found for Id: {avotype_id}".format(avotype_id=avotype_id),
        )

    elif (
        existing_avotype is not None and existing_avotype.typeid != avotype_id
    ):
        abort(
            409,
            "Avocado type {type} exists already".format(
                type=type
            ),
        )

    else:

        schema = AvoTypeSchema()
        update = schema.load(avotype, session=db.session)

        update.typeid = update_avotype.typeid

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_avotype)

        return data, 200


def delete(avotype_id):
    """
    This function deletes a person from the people structure
    :param person_id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    avotype = AvoType.query.filter(AvoType.typeid == avotype_id).one_or_none()

    if avotype is not None:
        db.session.delete(avotype)
        db.session.commit()
        return make_response(
            "Avocado Type {avotype_id} deleted".format(avotype_id=avotype_id), 200
        )

    else:
        abort(
            404,
            "Avocado Type not found for Id: {avotype_id}".format(avotype_id=avotype_id),
        )