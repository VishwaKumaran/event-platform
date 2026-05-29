from datetime import UTC, datetime
from uuid import uuid4

from pydantic import UUID4
from sqlmodel import Field, SQLModel, text


class EventMetric(SQLModel, table=True):
    id: UUID4 = Field(default_factory=lambda: uuid4(), primary_key=True)
    metric_name: str
    metric_value: int
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        nullable=False,
        index=True,
        sa_column_kwargs={
            "server_default": text("TIMEZONE('utc', now())"),
        },
    )
