# Created by khanhdh on 4/13/20
import enum
import logging

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from boilerplate.models import db, TimestampMixin

logger = logging.getLogger('main')


class Reaction(db.Model, TimestampMixin):
    __tablename__ = 'reactions'

    class Type(enum.Enum):
        LIKE = 'like'
        DISLIKE = 'dislike'
        LOVE = 'love'
        JOY = 'joy'
        SAD = 'sad'
        WOW = 'wow'
        ANGRY = 'angry'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Enum(Type), nullable=False)

    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='reactions')

    message_id = db.Column(db.Integer, ForeignKey('messages.id'), nullable=False)
    message = relationship('Message', back_populates='reactions')

    def to_dict(self):
        pass


class ReactionSchema:
    pass
