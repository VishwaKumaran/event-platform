from datetime import datetime
from typing import Any, Dict
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field


class EventSchema(BaseModel):
    event_id: UUID4 = Field(default_factory=uuid4)
    event_type: str
    user_id: UUID4
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: Dict[str, Any] = {}
