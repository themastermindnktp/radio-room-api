# Created by khanhdh on 4/13/20
import logging

from boilerplate import models

logger = logging.getLogger(__name__)


def save_user_to_database(**kwargs):
    user = models.User(**kwargs)
    models.db.session.add(user)

    return user
