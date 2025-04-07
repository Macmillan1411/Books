from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.models import User
from sqlmodel import select
from .schemas import UserSchema
from src.auth.utils import generate_password_hash, verify_password


class UserService:

    async def get_user_by_email(self, email: str, session: AsyncSession) -> UserSchema:
        statement = select(User).where(User.email == email)

        result = await session.exec(statement)
        user = result.first()

        return user



    async def user_exits(self, email: str, session: AsyncSession) -> bool:
        user = await self.get_user_by_email(email, session)

        if not user:
            return False
        return True


    async def create_user(self, user_data: User, session: AsyncSession) -> UserSchema:
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)
        new_user.password_hash = generate_password_hash(user_data_dict['password'])

        session.add(new_user)

        await session.commit()
        
        return new_user
