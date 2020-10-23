import signal
import asyncio
import functools
from typing import Callable

from loguru import logger
from fastapi import FastAPI

from app import settings
from app.core.logging import init_logger
from app.db.events import connect_to_db, close_db_connection
from app.exceptions.events import register_exceptions
from app.schedulers import load_jobs_with_lock
from app.services.events import start_engine, close_engine

HANDLED_SIGNALS = (
    signal.SIGINT,  # Unix signal 2. Sent by Ctrl+C.
    signal.SIGTERM,  # Unix signal 15. Sent by `kill <pid>`.
)


async def install_signal_handlers(app: FastAPI) -> None:
    # 当开发模式为dev时，添加监听命令行退出的信号
    if settings.env_for_dynaconf == "development":
        handle_exit_app = functools.partial(handle_exit, app)
        for sig in HANDLED_SIGNALS:
            signal.signal(sig, handle_exit_app)


def handle_exit(app: FastAPI, *args):
    # 关闭引擎
    asyncio.create_task(close_engine(app))


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await init_logger()
        await connect_to_db(app)
        await register_exceptions(app)
        await start_engine(app)
        await install_signal_handlers(app)
        await load_jobs_with_lock()
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    @logger.catch
    async def stop_app() -> None:
        await close_db_connection(app)
        await close_engine(app)
    return stop_app
