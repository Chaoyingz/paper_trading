from datetime import datetime
from typing import Optional

from pydantic import Field, PositiveInt, validator

from app.models.base import get_utc_now
from app.models.domain.position import Position, PositionInDB
from app.models.domain.stocks import Stock
from app.models.schemas.rwschema import RWSchema
from app.models.types import PyDecimal, PyObjectId


class PositionInCreate(RWSchema, Position):
    user: PyObjectId = Field(..., description="用户ID")


class PositionInManualCreate(RWSchema, Stock):
    volume: PositiveInt = Field(..., description="持仓数量")
    cost: PyDecimal = Field(..., description="成本价")


class PositionInResponse(RWSchema, PositionInDB):
    pass


class PositionInUpdateAvailable(RWSchema):
    id: PyObjectId = Field(..., description="ID")
    available_volume: int = Field(..., description="可卖数量")


class PositionInUpdate(RWSchema):
    id: PyObjectId = Field(..., description="ID")
    volume: int = Field(..., description="持仓数量")
    available_volume: int = Field(..., description="可卖数量")
    cost: PyDecimal = Field(..., description="持仓成本")
    current_price: PyDecimal = Field(..., description="当前价格")
    profit: PyDecimal = Field(..., description="利润")
    last_sell_date: datetime = Field(None, description="最后卖出日期")


class PositionInDelete(RWSchema):
    id: PyObjectId = Field(..., description="ID")


class PositionInCache(RWSchema, Stock):
    user: PyObjectId = Field(...)
    volume: int = Field(..., description="持仓数量")
    available_volume: int = Field(..., description="可卖数量")
    cost: PyDecimal = Field(..., description="持仓成本")
    current_price: PyDecimal = Field(..., description="当前价格")
    profit: PyDecimal = Field(..., description="利润")
    first_buy_date: Optional[datetime] = Field(None, description="首次持有日期")

    @validator("first_buy_date")
    def set_first_buy_date_default(cls, v):
        if not v:
            return get_utc_now()
        return v
