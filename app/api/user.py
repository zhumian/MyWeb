from flask import jsonify, request
from . import api
from ..models import User
from .. import db
from ..constant import response
from flask_login import login_required, current_user
import logging


@api.before_app_request
def before_request():
    logging.info(request)


@api.route("/user/save", methods=["POST"])
@login_required
def save():
    account = request.form.get("account")
    name = request.form.get("name")
    password = request.form.get("password")
    gender = int(request.form.get("gender"))
    user = User(account=account, name=name, password=password, gender=gender)
    db.session.add(user)
    db.session.commit()
    return jsonify(response(success=True, msg="操作成功"))


@api.route("/user/get", methods=["POST", "GET"])
@login_required
def get():
    id = request.form.get("id")
    user = User.query.get(id)
    if user is not None:
        return jsonify(response(data=user.to_json()))
    else:
        return jsonify(response(success=False))


@api.route("/user/queryAll", methods=["POST", "GET"])
@login_required
def query_all():
    users = User.query.all()
    return jsonify(response(success=True, data=[user.to_json() for user in users]))


