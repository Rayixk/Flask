# coding=utf-8
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from ext import db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

import users  # noqa

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
    """
    相关指令
    初次使用:python app_migrate.py db init
    迁移:python app_migrate.py db migrate
    更新:python app_migrate.py db upgrade  (此步会操作数据库)
    另:取消更改:python app_migrate.py db downgrade
    请注意:所有不在db管理的表,都会在迁移的过程中被删掉,所以,
    所有的模型文件都应该使用from ext import db来保证迁移时管理到所有的表.
    """
