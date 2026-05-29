from collections import defaultdict
from typing import Any, Dict

from lib.models import EventMetric

from core.db import get_session

event_counter = defaultdict(int)


async def process_event(event: Dict[str, Any]):
    event_type = event.get("event_type")
    user_id = event.get("user_id")

    event_counter[event_type] += 1

    print("EVENT COUNTS:")
    print(dict(event_counter))

    metric = EventMetric(metric_name=event_type, metric_value=event_counter[event_type])

    async with get_session() as session:
        session.add(metric)
        await session.commit()
