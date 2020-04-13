# Created by khanhdh on 4/13/20
import logging

from flask_restplus import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from boilerplate.models import db, TimestampMixin

logger = logging.getLogger(__name__)


class User(db.Model, TimestampMixin):
    __tablename__ = 'users'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(512), nullable=False)

    room_id = db.Column(db.Integer, ForeignKey('rooms.id'))
    room = relationship('Room', back_populates='users')

    songs = relationship('Song', back_populates='user')
    votes = relationship('Vote', back_populates='user')
    messages = relationship('Message', back_populates='user')
    reactions = relationship('Reaction', back_populates='user')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'token': self.token
        }


class UserSchema:
    user = {
        'id': fields.Integer(required=True, description='id'),
        'name': fields.String(required=True, description='name'),
        'token': fields.String(required=False, description='token')
    }

    user_create_req = {
        'name': fields.String(required=True, description='name')
    }
