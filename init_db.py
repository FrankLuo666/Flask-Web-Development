from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)
# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    # 清除数据库里所有的数据
    db.drop_all()
    # 创建所有的表
    db.create_all()

    # 创建对象
    role1 = Role(name="admin")
    # session记录对象任务
    db.session.add(role1)
    # 提交任务到数据库中
    db.session.commit()

    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    us1 = User(username='wang', role_id=role1.id)
    us2 = User(username='zhang', role_id=role2.id)
    us3 = User(username='chen', role_id=role2.id)
    us4 = User(username='zhou', role_id=role1.id)

    # 一次保存多条数据
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()