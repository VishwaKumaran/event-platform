from typing import List

from lib.models.event_metric import EventMetric

from core.db import get_session_context

buffer: List[EventMetric] = []
BATCH_SIZE = 10


async def add_event(event: EventMetric):
    buffer.append(event)
    if len(buffer) >= BATCH_SIZE:
        await flush()


async def flush():
    global buffer
    if not buffer:
        return

    async with get_session_context() as session:
        session.add_all(buffer)
        await session.commit()

    buffer = []
