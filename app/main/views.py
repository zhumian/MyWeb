from flask import render_template
from flask import request, jsonify, redirect, url_for
from . import main
from ..models import User
from ..constant import response
from flask_login import login_user, logout_user, login_required, current_user


@main.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@main.route("/login", methods=['POST'])
def login():
    account = request.form.get("account")
    password = request.form.get("password")
    user = User.query.filter_by(account=account).first()
    if user is None:
        return jsonify(response(success=False, msg="账号不存在"))
    if password != user.password:
        return jsonify(response(success=False, msg="密码错误"))
    login_user(user)
    return jsonify(response(success=True, msg="登录成功"))


@main.route("/logout", methods=["POST", "GET"])
def logout():
    logout_user()
    return redirect(url_for("main.index"))







