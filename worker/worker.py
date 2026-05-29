import asyncio
import json

import redis.asyncio as redis
from lib import redis_lifespan

from core.config import settings
from processor import process_event


async def create_consumer_group(redis_client: redis.Redis):
    try:
        await redis_client.xgroup_create(
            settings.REDIS_STREAM, settings.GROUP_NAME, id="0", mkstream=True
        )
        print("Consumer group created")

    except Exception:
        print("Consumer group already exists")


async def start_worker(redis_client: redis.Redis):
    print("Worker started")
    while True:
        events = await redis_client.xreadgroup(
            settings.GROUP_NAME,
            settings.CONSUMER_NAME,
            {settings.REDIS_STREAM: ">"},
            count=10,
            block=2000,
        )

        if not events:
            continue

        for _, messages in events:
            for message_id, data in messages:
                try:
                    event = json.loads(data["data"])

                    await process_event(event)

                    await redis_client.xack(
                        settings.REDIS_STREAM, settings.GROUP_NAME, message_id
                    )

                    print(f"ACK {message_id}")

                except Exception as e:
                    print(f"ERROR: {e}")


async def main():
    print("MAIN")
    async with redis_lifespan(settings.REDIS_URL, socket_timeout=10) as redis:
        await create_consumer_group(redis)
        await start_worker(redis)


if __name__ == "__main__":
    asyncio.run(main())
