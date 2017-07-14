# -*- coding: utf-8 -*-
from flask import Blueprint,render_template
from config import Config

mod = Blueprint('home',__name__)

@mod.route('/')
@mod.route('/index')
def index():
    return 'hello home!!!'

@mod.route('/store')
def store():
    return Config.APP_NAME
