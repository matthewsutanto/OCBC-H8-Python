from datetime import date
from config import db, ma
from marshmallow import fields
from sqlalchemy.orm import backref

class Avocado(db.Model):
    __tablename__ = 'avocado'
    date = db.Column(db.Date, default=date.utcnow)
    avgprice = db.Column(db.Real)
    totalvol = db.Column(db.Integer)
    avo_a = db.column(db.Integer)
    avo_b = db.column(db.Real)
    avo_c = db.column(db.Real)
    type = db.relationship(
        'Type',
        backref='avocado',
        cascade='all, delete, delete-orphan',
        single_parent=True
    )
    region = db.relationship(
        'Region',
        backref='avocado',
        cascade='all, delete, delete-orphan',
        single_parent=True
    )
    
class AvocadoRegion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer)
    region = db.Column(db.String(40))
    
class AvocadoType(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer)
    type = db.Column(db.String(40))
    
class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avocado
        sqla_session = db.session
        load_instance = True

    type = fields.Nested('AvocadoTypeSchema', default=[], many=True)
    

class AvocadoTypeSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    note_id = fields.Int()
    person_id = fields.Int()
    content = fields.Str()
    timestamp = fields.Str()


class NoteSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Note
        sqla_session = db.session

    person = fields.Nested("NotePersonSchema", default=None)