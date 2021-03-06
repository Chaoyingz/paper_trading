EXIT_ENGINE_EVENT = "exit_engine_event"  # 退出引擎事件

LOG_EVENT = "log_event"  # 推送日志

ORDER_CREATE_EVENT = "order_create_event"  # 新建订单
ORDER_UPDATE_EVENT = "order_update_event"  # 更新订单
ORDER_UPDATE_STATUS_EVENT = "order_update_status_event"  # 更新订单状态
ORDER_UPDATE_FROZEN_EVENT = "order_update_frozen_event"  # 更新订单冻结相关信息

STATEMENT_CREATE_EVENT = "statement_create_event"  # 创建交割单

USER_UPDATE_EVENT = "user_update_event"  # 更新用户信息
USER_UPDATE_AVAILABLE_CASH_EVENT = "user_update_available_cash_event"  # 更新用户可用现金
USER_UPDATE_ASSETS_EVENT = "user_update_assets_event"  # 更新用户资产

POSITION_CREATE_EVENT = "holding_stock_create_event"  # 新建持仓股票
POSITION_UPDATE_EVENT = "position_update_event"  # 更新持仓股票
POSITION_CLEAR_EVENT = "position_clear_event"  # 清仓

MARKET_CLOSE_EVENT = "market_close_event"  # 股市收盘事件
UNFREEZE_EVENT = "unfreeze_event"  # 解除预先冻结的现金或可用股票数量事件
