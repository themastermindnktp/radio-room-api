# coding=utf-8
import logging

from flask import request
from flask_restplus import Resource

from boilerplate import services, models
from boilerplate.extensions import Namespace

__author__ = 'ThucNC'
_logger = logging.getLogger(__name__)

user_namespace = Namespace('users', description='User operations')

_user_res = user_namespace.model('user_res', models.UserSchema.user)
_user_create_req = user_namespace.model('user_create_req',
                                        models.UserSchema.user_create_req)


@user_namespace.route('/', methods=['GET', 'POST'])
class Users(Resource):
    @user_namespace.expect(_user_create_req, validate=True)
    @user_namespace.marshal_with(_user_res)
    def post(self):
        data = request.args or request.json
        user = services.user.create_user(**data)

        return user
