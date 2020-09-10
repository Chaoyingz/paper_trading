from datetime import timedelta
import logging
import os

from flask.helpers import get_debug_flag

from paper_trading.trade.market import BacktestMarket, ChinaAMarket
from paper_trading.utility.constant import PersistanceMode, LoadDataMode


BASE_URL = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "j1as78a1gf6a4ea1f5d6a78e41fa56e"

    # 数据库设置
    MONGO_HOST: str = "localhost"
    MONGO_PORT: int = 27017
    ACCOUNT_DB: str = "pt_account"
    POSITION_DB: str = "pt_position"
    TRADE_DB: str = "pt_trade"
    ACCOUNT_RECORD: str = "pt_acc_record"
    POS_RECORD: str = "pt_pos_record"

    LOG_FILE_NAME: str = ""
    LOG_FILE_PATH: str = ""
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 5000

    # 设置session的保存时间。
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # 设置ROOT目录
    ROOT_PATH = os.path.join(BASE_URL, "app")

    # 市场名称
    MARKET_NAME: str = ""
    # 账户token长度
    TOKEN_LENGTH: int = 20
    # 数据精确度
    POINT: int = 2
    # 是否开启成交量计算模拟
    # TODO 暂时没有实现相关功能
    VOLUME_SIMULATION: bool = False
    # 是否开启账户与持仓信息的验证
    VERIFICATION: bool = True
    # 引擎撮合速度（秒）
    # 设置此参数时请参考行情的刷新速度
    PERIOD: int = 3

    # 数据持久化模式
    # 实时持久化，会大幅降低整个模拟交易程序的执行效率，建议在手工交易时使用
    # 定时持久化，系统会在指定的时间间隔进行自动持久化，时间间隔越低，效率越低，建议进行低频程序化交易时使用
    # 手动持久化，系统会在接收到命令时进行持久化操作，建议在回测时使用
    PERSISTENCE_MODE: str = ""
    # 数据加载参数，默认交易模式
    LOAD_DATA_MODE = LoadDataMode.TRADING
    market = ChinaAMarket
    # 数据持久化时间间隔
    # TODO 暂时没有实现相关功能
    P_TIMING: int = 0

    # tushare行情源参数(填写你自己的tushare token，可以前往https://tushare.pro/ 注册申请)
    TUSHARE_TOKEN: str = ""

    # pytdx行情参数（可以去各家券商下载通达信交易软件找到相关的地址）
    TDX_HOST: str = "210.51.39.201"
    TDX_PORT: int = 7709

    # 账户初始参数
    CAPITAL: float = 1000000.00     # 初始资金
    COST: float = 0.0003            # 交易佣金
    TAX: float = 0.001              # 印花税
    SLIPPOINT: float = 0.01         # 滑点（暂未实现）

    # log服务参数
    LOG_ACTIVE: bool = True
    LOG_LEVEL: bool = DEBUG
    LOG_CONSOLE: bool = True

    # email服务参数(根据实际情况进行使用）
    EMAIL_SERVER: str = ""
    EMAIL_PORT: str = ""
    EMAIL_USERNAME: str = ""
    EMAIL_PASSWORD: str = ""
    EMAIL_SENDER: str = ""
    EMAIL_RECEIVER: str = ""

    LOG_FORMAT = {
        "version": 1,
        "formatters": {"default": {"format": "[%(name)s][%(asctime)s] %(levelname)s in %(module)s: %(message)s"}},
        "handlers": {"wsgi": {"class": "logging.StreamHandler", "stream": "ext://flask.logging.wsgi_errors_stream",
                              "formatter": "default"}},
        "loggers": {
            "flask.app": {"level": logging.WARNING},
            "lazyTrader": {"level": logging.WARNING},
            "werkzeug": {"level": logging.WARNING},
            "apscheduler.scheduler": {"level": logging.WARNING},
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class TestConfig(Config):
    PERSISTENCE_MODE = PersistanceMode.MANUAL
    LOAD_DATA_MODE = LoadDataMode.BACKTEST
    market = BacktestMarket


class DevConfig(Config):
    DEBUG = True
    PERSISTENCE_MODE = PersistanceMode.MANUAL
    LOAD_DATA_MODE = LoadDataMode.BACKTEST
    market = BacktestMarket


config = DevConfig if get_debug_flag() else ProdConfig