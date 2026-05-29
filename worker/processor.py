from collections import defaultdict
from typing import Any, Dict

from lib.models import EventMetric

from core.db import get_session

event_counter = defaultdict(int)


async def process_event(event: Dict[str, Any]):
    event_type: str = event["event_type"]
    user_id = event["user_id"]

    event_counter[event_type] += 1

    print("EVENT COUNTS:")
    print(dict(event_counter))

    metric = EventMetric(metric_name=event_type, metric_value=event_counter[event_type])

    async with get_session() as session:
        session.add(metric)
        await session.commit()


if __name__ == "__main__":

    async def main():
        await process_event(
            {
                "event_type": "click",
                "user_id": "1cfce037-44f1-4907-a512-c008ea426099",
                "metadata": {"page": "home", "button": "signin"},
            }
        )

    import asyncio

    asyncio.run(main())
