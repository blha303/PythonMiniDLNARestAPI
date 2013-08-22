# Requirements (rather, the versions of these requirements that I have):
# Flask==0.10.1
# Flask-Restless==0.12.0
# Flask-SQLAlchemy==1.0
# SQLAlchemy==0.8.2

# Run this on the media server. It runs on port 5000 by default.

# Copyright 2013 Steven Smith (blha303). All Rights Reserved.
# New BSD license
# http://www.opensource.org/licenses/BSD-3-Clause

import flask
import flask.ext.sqlalchemy
app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////var/lib/minidlna/files.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

class Details(db.Model):
    __tablename__ = "DETAILS"
    ID = db.Column(db.Integer, primary_key=True)
    PATH = db.Column(db.Text)
    SIZE = db.Column(db.Integer)
    TIMESTAMP = db.Column(db.Integer)
    TITLE = db.Column(db.Text)
    DURATION = db.Column(db.Text)
    BITRATE = db.Column(db.Integer)
    SAMPLERATE = db.Column(db.Integer)
    CREATOR = db.Column(db.Text)
    ARTIST = db.Column(db.Text)
    ALBUM = db.Column(db.Text)
    GENRE = db.Column(db.Text)
    COMMENT = db.Column(db.Text)
    CHANNELS = db.Column(db.Integer)
    DISC = db.Column(db.Integer)
    TRACK = db.Column(db.Integer)
    DATE = db.Column(db.Date)
    RESOLUTION = db.Column(db.Text)
    THUMBNAIL = db.Column(db.Boolean)
    ALBUM_ART = db.Column(db.Integer)
    ROTATION = db.Column(db.Integer)
    DLNA_PN = db.Column(db.Text)
    MIME = db.Column(db.Text)

import flask.ext.restless

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Details, methods=['GET'], results_per_page=20)

app.run(host='0.0.0.0')
