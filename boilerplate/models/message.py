# Created by khanhdh on 4/13/20
import logging

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from boilerplate.models import db, TimestampMixin

logger = logging.getLogger('main')


class Message(db.Model, TimestampMixin):
    __tablename__ = 'messages'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)

    room_id = db.Column(db.Integer, ForeignKey('rooms.id'))
    room = relationship('Room', back_populates='messages')

    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='messages')

    reactions = relationship('Reaction', back_populates='message')

    def to_dict(self):
        pass


class MessageSchema:
    pass
