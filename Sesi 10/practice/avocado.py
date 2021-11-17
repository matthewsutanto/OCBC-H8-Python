"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Avocado, AvoType, AvoRegion ,AvocadoSchema


def read_all():
    """
    This function responds to a request for /api/people/notes
    with the complete list of notes, sorted by note timestamp

    :return:                json list of all notes for all people
    """
    avocados = Avocado.query.order_by(db.desc(Avocado.id)).all()
    
    avocado_schema = AvocadoSchema(many=True)
    data = avocado_schema.dump(avocados)
    return data


def read_one(id):
    """
    This function responds to a request for
    /api/people/{person_id}/notes/{note_id}
    with one matching note for the associated person

    :param person_id:       Id of person the note is related to
    :param note_id:         Id of the note
    :return:                json string of note contents
    """
    avocado = (
        Avocado.query.join(AvoType, AvoType.typeid == Avocado.type)
        .join(AvoRegion, AvoRegion.regionid == Avocado.region)
        .filter(Avocado.id == id)
        .one_or_none()
    )

    if avocado is not None:
        avocado_schema = AvocadoSchema()
        data = avocado_schema.dump(avocado)
        return data

    else:
        abort(404, f"Avocado not found for Id: {id}")


def create(typeid, regionid, avocado):
    """
    This function creates a new note related to the passed in person id.

    :param person_id:       Id of the person the note is related to
    :param note:            The JSON containing the note data
    :return:                201 on success
    """
    avoType = AvoType.query.filter(AvoType.typeid == typeid).one_or_none()

    if avoType is None:
        abort(404, f"Type is not found for Id: {typeid}")
        
    avoRegion = AvoRegion.query.filter(AvoRegion.regionid == regionid).one_or_none()

    if avoRegion is None:
        abort(404, f"Type is not found for Id: {regionid}")
        

    schema = AvocadoSchema()
    new_avocado = schema.load(avocado, session=db.session)

    avoType.avocado.append(new_avocado)
    avoRegion.avocado.append(new_avocado)
    db.session.commit()

    data = schema.dump(new_avocado)

    return data, 201


def update(id, avocado):
    """
    This function updates an existing note related to the passed in
    person id.

    :param person_id:       Id of the person the note is related to
    :param note_id:         Id of the note to update
    :param content:            The JSON containing the note data
    :return:                200 on success
    """
    update_avocado = (
        Avocado.query.join(AvoType, AvoType.typeid == Avocado.type)
        .join(AvoRegion, AvoRegion.regionid == Avocado.region)
        .filter(Avocado.id == id)
        .one_or_none()
    )

    if update_avocado is not None:

        schema = AvocadoSchema()
        update = schema.load(avocado, session=db.session)

        update.id = update_avocado.id
        update.type = update_avocado.type
        update.region = update_avocado.region
        
        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_avocado)

        return data, 200

    else:
        abort(404, f"Avocado not found for Id: {id}")


def delete(id):
    """
    This function deletes a note from the note structure

    :param person_id:   Id of the person the note is related to
    :param note_id:     Id of the note to delete
    :return:            200 on successful delete, 404 if not found
    """
    avocado = Avocado.query.filter(Avocado.id == id).one_or_none()

    if avocado is not None:
        db.session.delete(avocado)
        db.session.commit()
        return make_response(
            "Avocado {id} deleted".format(id=id), 200
        )

    else:
        abort(
            404,
            "Avocado not found for Id: {id}".format(id=id),
        )