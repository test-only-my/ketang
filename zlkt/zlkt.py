# encoding:utf-8
from flask import Flask,render_template,request,redirect,url_for,session
import config
from exts import db
from models import *

app = Flask(__name__)
app.config.from_object(config)
# 初始化app
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone==telephone).first()
        if user:
            if password == user.password:
                session['user_id'] = user.id
                # 设置默认登录时间一个月即31天
                # session.permanent = True
                return redirect(url_for('index'))
            else:
                return '用户名或密码错误！'


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephone==telephone).first()
        # 校验重复注册
        if user:
            return '该用户已被注册！'
        else:
            if password1 != password2:
                return '两次密码输入不一致！'
            else:
                # 存入数据库，并跳转到登录页面
                user = User(username=username,telephone=telephone,password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))

@app.context_processor
def if_login_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id==user_id).first()
        if user:
            return {'user':user}
    return {}

@app.route('/question')
def question():
    return render_template('question.html')

if __name__ == '__main__':
    app.run()
