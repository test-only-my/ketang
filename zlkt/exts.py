# encoding:utf-8
# db和视图函数，解决循环引用的问题，创建中间这个文件
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()