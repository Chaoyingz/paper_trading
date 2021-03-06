from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.exceptions import http


def register_exceptions(app: FastAPI) -> Callable:
    def inner():
        """注册自定义HTTP异常"""
        app.add_exception_handler(http.InvalidUserID, http.InvalidUserID.handler)
        app.add_exception_handler(
            http.InvalidAuthTokenPrefix, http.InvalidAuthTokenPrefix.handler
        )
        app.add_exception_handler(
            http.AuthHeaderNotFound, http.AuthHeaderNotFound.handler
        )
        app.add_exception_handler(http.InvalidAuthToken, http.InvalidAuthToken.handler)
        app.add_exception_handler(http.WrongTokenFormat, http.WrongTokenFormat.handler)
        app.add_exception_handler(http.InvalidAuthMode, http.InvalidAuthMode.handler)
        app.add_exception_handler(http.OrderFailed, http.OrderFailed.handler)
        app.add_exception_handler(
            http.InvalidOrderExchange, http.InvalidOrderExchange.handler
        )
        app.add_exception_handler(http.OrderNotFound, http.OrderNotFound.handler)
        app.add_exception_handler(http.NotTradingTime, http.NotTradingTime.handler)
        app.add_exception_handler(
            http.CancelOrderFailed, http.CancelOrderFailed.handler
        )
        logger.info("注册自定义HTTP异常类别完成.")

    return inner
