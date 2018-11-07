from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager
from flask_login import UserMixin, AnonymousUserMixin
import logging


class User(db.Model, UserMixin):
    __tablename__ = 'tb_user'
    id = db.Column(db.INT, primary_key=True)
    account = db.Column(db.String(50))
    name = db.Column(db.String(50))
    password = db.Column(db.String(255))
    gender = db.Column(db.INT)
    create_time = db.Column(db.DATETIME)
    creator_id = db.Column(db.INT)
    creator_name = db.Column(db.String(50))
    update_time = db.Column(db.DATETIME)
    updater_id = db.Column(db.INT)
    updater_name = db.Column(db.String(50))

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return repr(self.id, self.account, self.name, self.gender,
                    self.create_time, self.creator_id, self.creator_name,
                    self.update_time, self.updater_id, self.updater_name)

    def to_json(self):
        return dict(
            id=self.id,
            account=self.account,
            name=self.name,
            create_time=self.create_time,
            creator_id=self.creator_id,
            creator_name=self.creator_name,
            update_time=self.update_time,
            updater_id=self.updater_id,
            updater_name=self.updater_name
        )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))







