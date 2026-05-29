from datetime import datetime, timezone
from uuid import uuid4

from pydantic import UUID4
from sqlmodel import Field, SQLModel, text


class EventMetric(SQLModel, table=True):
    id: UUID4 = Field(default_factory=lambda: uuid4(), primary_key=True)
    metric_name: str
    metric_value: int
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        index=True,
        sa_column_kwargs={
            "server_default": text("now()"),
        },
    )
