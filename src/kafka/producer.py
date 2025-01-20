import json
from typing import Any

from aiokafka import AIOKafkaProducer


class KafkaProducer:
    producer = None
    KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092'
    KAFKA_TOPIC = 'applications'

    async def producer_start(self) -> None:
        if self.producer is None:
            self.producer = AIOKafkaProducer(bootstrap_servers=self.KAFKA_BOOTSTRAP_SERVERS)
            await self.producer.start()

    async def producer_stop(self) -> None:
        if self.producer:
            await self.producer.stop()
            self.producer = None

    async def send_message(self, message: dict[str, Any]) -> None:
        try:
            await self.producer.send_and_wait(self.KAFKA_TOPIC, value=json.dumps(message).encode('utf-8'))
        except Exception as e:
            raise e


kafka = KafkaProducer()
