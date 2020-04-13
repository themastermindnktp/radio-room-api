# coding=utf-8
import logging

__author__ = 'Kien'

from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

_logger = logging.getLogger(__name__)

db = SQLAlchemy()
migrate = Migrate(db=db)
bcrypt = Bcrypt()


def init_app(app, **kwargs):
    """
    Extension initialization point
    :param flask.Flask app:
    :param kwargs:
    :return:
    """
    db.app = app
    db.init_app(app)
    migrate.init_app(app)
    _logger.info('Start app in {env} environment with database: {db}'.format(
        env=app.config['ENV_MODE'],
        db=app.config['SQLALCHEMY_DATABASE_URI']
    ))


from .base import TimestampMixin
from .room import Room, RoomSchema
from .user import User, UserSchema
from .song import Song, SongSchema
from .vote import Vote, VoteSchema
from .message import Message, MessageSchema
from .reaction import Reaction, ReactionSchema
