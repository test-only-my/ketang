# encoding:utf-8
# from flask_sqlalchemy import SQLAlchemy
from exts import db
# 创建模型文件

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    telephone = db.Column(db.String(11),nullable=False)
