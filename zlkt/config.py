# encoding:utf-8
from flask import Flask
from zlkt import app


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

