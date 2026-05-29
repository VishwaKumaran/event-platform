from datetime import UTC, datetime
from uuid import uuid4

from pydantic import UUID4
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Column, Field, SQLModel, text


class Event(SQLModel, table=True):
    id: UUID4 = Field(default_factory=lambda: uuid4(), primary_key=True)
    event_type: str
    user_id: UUID4
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        nullable=False,
        index=True,
        sa_column_kwargs={
            "server_default": text("TIMEZONE('utc', now())"),
        },
    )
    data: dict = Field(
        default_factory=dict,
        sa_column=Column(JSONB, nullable=False, server_default=text("'{}'")),
    )
