# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from apps import create_app
from apps import db
from apps.models import User, Member
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

# http://www.jianshu.com/p/032723bb9b05  数据库迁移
# from apps import socketio
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    # socketio.run(app)