from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class User(db.Model):
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

    @property
    def password(self):
        pass

    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)





