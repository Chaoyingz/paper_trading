from typing import List

from app import settings
from app.db.repositories.base import BaseRepository

from app.exceptions.db import EntityDoesNotExist
from app.models.domain.users import UserInDB
from app.models.types import PyObjectId


class UsersRepository(BaseRepository):
    COLLECTION_NAME = settings.db.collections.user

    async def create_user(self, *, capital: float, desc: str = "") -> UserInDB:
        user = UserInDB(capital=capital, desc=desc, assets=capital, cash=capital)
        user_row = await self.collection.insert_one(user.dict(exclude={"id"}))
        user.id = user_row.inserted_id
        return user

    async def get_user_by_id(self, *, user_id: str) -> UserInDB:
        user_row = await self.collection.find_one({"_id": PyObjectId(user_id)})
        if user_row:
            return UserInDB(**user_row)
        raise EntityDoesNotExist(f"用户`{user_id}`不存在.")

    async def get_users_list(self) -> List[UserInDB]:
        users_row = self.collection.find({})
        return [UserInDB(**user) async for user in users_row]

    async def update_user_by_id(
        self,
        capital: float,
        assets: float,
        cash: float,
        securities: float,
        commission: float,
        tas: float,
        slippage: float,
        desc: str = ""
    ):
        pass