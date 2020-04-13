# Created by khanhdh on 4/13/20
import logging

from boilerplate import repositories
from boilerplate.extensions.exceptions import BadRequestException

_logger = logging.getLogger(__name__)


def create_user(name, **kwargs):
    # TODO: validate name and set token
    # if is_not_valid_name(name):
    #     raise BadRequestException("Invalid user data specified!")
    user = repositories.user.save_user_to_database(
        name=name,
        # token=token,
        **kwargs
    )
    return user

