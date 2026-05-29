from uuid import uuid4

from pydantic import UUID4
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: UUID4 = Field(default_factory=lambda: uuid4(), primary_key=True)
    username: str = Field(index=True, nullable=False, unique=True)
    email: str = Field(index=True, nullable=False, unique=True)
    hashed_password: str
    disabled: bool = False
