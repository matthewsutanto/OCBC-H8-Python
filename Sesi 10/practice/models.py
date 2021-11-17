from datetime import date
from config import db, ma
from marshmallow import fields

class Avocado(db.Model):
    __tablename__ = 'avocado'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today())
    avgprice = db.Column(db.Integer)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Integer)
    avo_c = db.Column(db.Integer)
    type = db.Column(db.Integer, db.ForeignKey('avotype.typeid'))
    region = db.Column(db.Integer, db.ForeignKey('avoregion.regionid'))
    
class AvoRegion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(40))
    
    avocado = db.relationship(
        'Avocado',
        backref='avoregion',
        cascade='all, delete, delete-orphan',
        single_parent=True
    )
    
class AvoType(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(40))
    
    avocado = db.relationship(
        'Avocado',
        backref='avotype',
        cascade='all, delete, delete-orphan',
        single_parent=True
    )
    
class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avocado
        sqla_session = db.session
        load_instance = True

    type = fields.Nested("AvocadoAvoTypeSchema", default=None)
    region = fields.Nested("AvocadoAvoRegionSchema", default=None)
    
class AvocadoAvoTypeSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    typeid = fields.Int()
    type = fields.Str()


class AvoTypeSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = AvoType
        sqla_session = db.session
        load_instance = True

    avocado = fields.Nested("AvoTypeAvocadoSchema", default=[], many=True)

class AvoTypeAvocadoSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    id = fields.Int()
    date = fields.Date()
    avgprice = fields.Int()
    totalvol = fields.Int()
    avo_a = fields.Int()
    avo_b = fields.Int()
    avo_c = fields.Int()
    type = fields.Int()
    region = fields.Int()

class AvocadoAvoRegionSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    regionid = fields.Int()
    region = fields.Str()


class AvoRegionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = AvoType
        sqla_session = db.session
        load_instance = True

    avocado = fields.Nested("AvoRegionAvocadoSchema", default=[], many=True)

class AvoRegionAvocadoSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    id = fields.Int()
    date = fields.Date()
    avgprice = fields.Int()
    totalvol = fields.Int()
    avo_a = fields.Int()
    avo_b = fields.Int()
    avo_c = fields.Int()
    type = fields.Int()
    region = fields.Int()