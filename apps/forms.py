# -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import StringField , BooleanField , PasswordField , SubmitField,ValidationError
from wtforms.validators import DataRequired,Required,Length,Email,EqualTo,Regexp

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired(message=u'用户名不能为空')])
    password = PasswordField('password', validators=[DataRequired(message=u'密码不能为空')])

# class LoginForm(FlaskForm):
#     email = StringField(u'邮箱', validators=[
#                 DataRequired(message= u'邮箱不能为空'), Length(1, 64),
#                 Email(message= u'请输入有效的邮箱地址，比如：username@domain.com')])
#     password = PasswordField(u'密码',
#                   validators=[Required(message= u'密码不能为空')])
#     submit = SubmitField(u'登录')