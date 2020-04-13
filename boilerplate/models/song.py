# Created by khanhdh on 4/13/20
import logging

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from boilerplate.models import db, TimestampMixin

logger = logging.getLogger('main')


class Song(db.Model, TimestampMixin):
    __tablename__ = 'songs'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.String(512), nullable=False)
    number_of_upvotes = db.Column(db.Integer)
    number_of_downvotes = db.Column(db.Integer)

    room_id = db.Column(db.Integer, ForeignKey('rooms.id'))
    room = relationship('Room', back_populates='songs')

    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='songs')

    votes = relationship('Vote', back_populates='song')

    def to_dict(self):
        pass


class SongSchema:
    song = {}
