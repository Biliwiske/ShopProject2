
import aio_pika
import json
import traceback
from asyncio import AbstractEventLoop
from aio_pika.abc import AbstractRobustConnection
from aio_pika import IncomingMessage
from uuid import UUID

from app.settings import settings
from app.services.product_service import ProductService
from app.repositories.db_product_repo import ProductRepo


async def process_created_product(msg: IncomingMessage):
    try:
        data = json.loads(msg.body.decode())
        print("\n/// process_created_product ///\n ")
        ProductService(productRepo()).create_product(
            data['order_id'], data['name'], data['brand'], data['price'])
        await msg.ack()
    except:
        traceback.print_exc()
        await msg.ack()


async def consume(loop: AbstractEventLoop) -> AbstractRobustConnection:
    connection = await aio_pika.connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()

    product_created_queue = await channel.declare_queue('product_created_queue', durable=True)

    await product_created_queue.consume(process_created_product)

    print('Started RabbitMQ consuming...')

    return connection
