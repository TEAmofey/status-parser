import asyncio

from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest

from config import telethon_data
import logging

from time import sleep


# Присваиваем значения внутренним переменным


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

my_user_id = 447873267

statuses_old = {my_user_id: ""}
statuses_new = {my_user_id: ""}


async def parse(client: TelegramClient, user_id: int):
    user_info = await client(GetFullUserRequest(id=user_id))
    status = user_info.full_user.about
    if status is None:
        status = ""
    statuses_new[user_id] = status


async def dump_statuses_every_minute():
    while True:
        await telethon_data.client.connect()
        await parse(telethon_data.client, my_user_id)
        if statuses_new[my_user_id] != statuses_old[my_user_id]:
            await telethon_data.client.send_message("mofeytea_statuses", statuses_new[my_user_id])
            statuses_old[my_user_id] = statuses_new[my_user_id]
        await telethon_data.client.disconnect()
        sleep(5)


async def loop_a():
    telethon_data.client = TelegramClient(
        telethon_data.username,
        telethon_data.api_id,
        telethon_data.api_hash
    )
    telethon_data.client.start(
        lambda: telethon_data.bot_token
    )
    await telethon_data.client.connect()
    await telethon_data.client.disconnect()
    await dump_statuses_every_minute()


async def main():
    task1 = asyncio.create_task(loop_a())

    await task1


if __name__ == '__main__':
    asyncio.run(main())
