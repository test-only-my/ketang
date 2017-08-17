# encoding:utf-8
from flask import Flask



debug = True
SECRET_KEY = '1'

# 数据库配置
# 'mysql+mysqldb://root:mysql@127.0.0.1:3306/test3'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'mysql'
HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'zlkt'
SQLALCHEMY_DATABASE_URI = 'mysql+{}://{}:{}@{}:{}/{}'.format(DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
# 避免警告:设置成 True，SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = True
