from datetime import datetime, timezone
from uuid import uuid4

from pydantic import UUID4
from sqlmodel import Column, DateTime, Field, Index, SQLModel


class EventMetric(SQLModel, table=True):
    id: UUID4 = Field(default_factory=lambda: uuid4(), primary_key=True)
    metric_name: str = Field(index=True)
    metric_value: int
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )

    __table_args__ = (Index("idx_event_user_id_timestamp", "metric_name", "timestamp"),)
