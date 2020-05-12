from flask import Flask
from datetime import timedelta

from paper_trading.config import config
from paper_trading.tasks.base import init_tasks
from .views import init_blue


def creat_app(config_name: str, engine):
    __all__ = ['app']
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config[config_name].SECRET_KEY

    # 设置session的保存时间。
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

    # 注册蓝本
    init_blue(app, engine)
    # 注册定时任务
    init_tasks(app, engine)
    return app
