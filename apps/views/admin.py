# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, session, redirect, url_for
from apps import db # ,socketio
from apps.models import User
from flask import flash,current_app
from flask_login import login_user, login_required, logout_user
from apps.forms import LoginForm

from flask_socketio import emit, send

__author__ = '陈偲'

mod = Blueprint('admin', __name__)

# 首页
@mod.route('/')
@mod.route('/index')
@login_required
def index():
    # 你可以使用‘success’、‘info’、‘warning’、‘danger’这四个值中的任一个。具体样式见下面的图片，从上到下依次为：‘success’、‘info’、‘warning’、‘danger’。
    # flash(u'this is info', 'info')
    # flash(u'this is success', 'success')
    # flash(u'this is warning', 'warning')
    # flash(u'this is danger', 'danger')
    return render_template('admin/index.html')

# 登录页面
@mod.route('/login',methods=['POST', 'GET'])
def login():
    form = LoginForm()
    title = '登录'
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        password = request.form['password']
        if user is not None and user.verify_password(password):
            remember = request.form.get("remember")
            login_user(user, remember)
            # session['name'] = username
            # session['user_id'] = user.id
            flash('欢迎回来', 'success')
            return redirect(request.args.get('next') or url_for('admin.index'))
        else:
            flash('用户名或者密码错误','warning')
            return render_template('admin/login.html', form=form, title=title)
    else:
        return render_template('admin/login.html', form=form, title=title)

# 退出登录
@mod.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经退出系统','success')
    return redirect(url_for('admin.index'))

@mod.route('/hello')
def hello():
    return render_template('admin/hello.html')

# @socketio.on('client_event')
# def client_msg(msg):
#     sid = request.sid
#     emit('server_response', {'data': str(sid)})

# @socketio.on('connect_event')
# def connected_msg(msg):
#     emit('server_response', {'data': msg['data']})

