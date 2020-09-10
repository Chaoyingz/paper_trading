from flask import Flask

from paper_trading.settings import config
from paper_trading.trade.pt_engine import MainEngine
from paper_trading.tasks.base import init_tasks
from paper_trading.app.views import init_blue


def create_app():
    # 创建app实例前先配置好日志文件
    app = Flask(__name__.split('.')[0], root_path=config.ROOT_PATH)
    app.config.from_object(config)

    engine = MainEngine()

    # 注册蓝本
    init_blue(app, engine)
    # 注册定时任务
    init_tasks(app, engine)
    return app
