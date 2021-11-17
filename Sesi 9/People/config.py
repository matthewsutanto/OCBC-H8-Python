import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ndyvbawytmftsz:cb04c74f0077c539b52df5443726d5bcd079dbdd6ca27a6ba63b9d98f4f384d4@ec2-3-228-134-188.compute-1.amazonaws.com:5432/d8jpdalkuitavh"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)