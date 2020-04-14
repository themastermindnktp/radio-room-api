# Created by khanhdh on 4/13/20
import logging

from flask_restplus import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from boilerplate.models import db, bcrypt
from boilerplate.models.base import TimestampMixin

logger = logging.getLogger('main')


class Room(db.Model, TimestampMixin):
    __tablename__ = 'rooms'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    has_password = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(255))
    number_of_users = db.Column(db.Integer)
    descriptions = db.Column(db.JSON)

    current_song = db.Column(db.String(512))
    current_song_start_time = db.Column(db.TIMESTAMP)

    creator_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    creator = relationship('User')

    users = relationship('User', backref='room')
    songs = relationship('Song', backref='room')
    messages = relationship('Message', backref='room')

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self):
        # TODO: add more visible attributes
        return {
            'id': self.id,
            'name': self.name,
            'has_password': self.has_password,
            'number_of_users': self.number_of_users,
            'descriptions': self.descriptions
        }


class RoomSchema:
    room = {
        'id': fields.Integer(required=True, description='id'),
        'name': fields.String(required=True, description='name'),
        'has_password': fields.String(required=False, description='has password'),
        'number_of_users': fields.Integer(required=False, description='number of users'),
        'descriptions': fields.String(required=False, description='descriptions')
    }

    room_create_req = room.copy()
    room_create_req.pop('id')
    room_create_req.pop('number_of_users')
    room_create_req.update({
        'password': fields.String(required=False, description='password')
    })
