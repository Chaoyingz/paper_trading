EXIT_ENGINE_EVENT = "exit_engine_event"  # 退出引擎事件

LOG_EVENT = "log_event"  # 推送日志

ORDER_CREATE_EVENT = "order_create_event"  # 新建订单
ORDER_UPDATE_EVENT = "order_update_event"  # 更新订单
ORDER_UPDATE_STATUS_EVENT = "order_update_status_event"  # 更新订单状态
ORDER_UPDATE_FROZEN_EVENT = "order_update_frozen_event"  # 更新订单冻结相关信息

USER_UPDATE_CASH_EVENT = "user_update_cash_event"  # 更新用户可用现金
USER_UPDATE_EVENT = "user_update_event"  # 更新用户信息

POSITION_CREATE_EVENT = "holding_stock_create_event"  # 新建持仓股票
POSITION_UPDATE_AVAILABLE_EVENT = "position_update_available_event"  # 更新持仓股票可用数量
POSITION_UPDATE_EVENT = "position_update_event"  # 更新持仓股票
POSITION_CLEAR_EVENT = "position_clear_event"  # 清仓

USER_ASSETS_RECORD_CREATE_EVENT = "user_assets_record_create_event"  # 创建用户资产记录
USER_ASSETS_RECORD_UPDATE_EVENT = "user_assets_record_update_event"  # 更新用户资产记录

MARKET_CLOSE_EVENT = "market_close_event"  # 股市收盘事件
UNFREEZE_EVENT = "unfreeze_event"   # 解除预先冻结的现金或可用股票数量事件
