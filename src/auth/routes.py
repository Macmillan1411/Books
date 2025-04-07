from fastapi import APIRouter, Depends, status
from .schemas import UserSchema, UserCreateSchema
from .service import UserService
from sqlalchemy.ext.asyncio import AsyncSession
from src.books.db.main import get_session


auth_router = APIRouter()
user_service = UserService()


@auth_router.post(
    "/signup", response_model=UserSchema, status_code=status.HTTP_201_CREATED
)
async def create_user_account(
    user_data: UserCreateSchema, session: AsyncSession = Depends(get_session)
) -> UserSchema:
    email = user_data.email

    user_exists = await user_service.user_exits(email, session)

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User with email already exists",
        )

    new_user = await user_service.create_user(user_data, session)

    return new_user
