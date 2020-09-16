import datetime
from decimal import Decimal, localcontext

from bson import ObjectId, Decimal128
from pydantic import BaseModel, BaseConfig


def convert_datetime_to_str(dt: datetime.datetime) -> str:
    return dt.replace(tzinfo=datetime.timezone.utc).isoformat().replace("+00:00", "Z")


class RWModel(BaseModel):
    """模型基类"""
    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {
            datetime.datetime: convert_datetime_to_str,
            ObjectId: lambda x: x.__str__(),
        }


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(pattern="^[0-9a-fA-F]{24}$", examples=["5f365bedcf31136279a97d19",
                                                                   "5d883e0bedcac5082ecf3afa"])

    @classmethod
    def validate(cls, v):
        if not isinstance(v, cls):
            if not cls.is_valid(v):
                raise TypeError(f"Not a valid ObjectId: {v}")
            return cls(v)
        return cls(v)


class PyDecimal(Decimal128):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """转化float为Decimal128
        先将python的二进制浮点数用str方法转化为10进制字符串，再把字符串转化为Decimal128
        """
        if not isinstance(v, float):
            raise TypeError(f"Cannot convert {v} to Decimal128")
        return cls(str(v))

