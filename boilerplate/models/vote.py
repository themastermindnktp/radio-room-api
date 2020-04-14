# Created by khanhdh on 4/13/20
import enum
import logging

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from boilerplate.models import db, TimestampMixin

logger = logging.getLogger('main')


class Vote(db.Model, TimestampMixin):
    __tablename__ = 'votes'

    class Type(enum.Enum):
        UPVOTE = 'upvote'
        DOWNVOTE = 'downvote'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Enum(Type), nullable=False)

    song_id = db.Column(db.Integer, ForeignKey('songs.id'), nullable=False)
    song = relationship('Song', back_populates='votes')

    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='songs')

    def to_dict(self):
        pass


class VoteSchema:
    pass
