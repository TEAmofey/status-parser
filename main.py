import asyncio

from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest

from config import telethon_data
import logging

from time import sleep

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


async def parse(client: TelegramClient, user_id: int):
    user_info = await client(GetFullUserRequest(id=user_id))
    status = user_info.full_user.about
    return status if status is not None else ""


async def dump_statuses_every_n_sec(user_id: int, n: int = 3600):
    await telethon_data.client.connect()
    status = await parse(telethon_data.client, user_id)
    await telethon_data.client.disconnect()

    while True:
        await telethon_data.client.connect()
        new_status = await parse(telethon_data.client, user_id)
        if new_status != status:
            await telethon_data.client.send_message("statuses_mofeytea", new_status)
            status = new_status
        await telethon_data.client.disconnect()
        sleep(n)


async def main():
    my_user_id = 447873267

    telethon_data.client = TelegramClient(
        "sessions/session_master",
        telethon_data.api_id,
        telethon_data.api_hash
    )
    await telethon_data.client.start(
        lambda: telethon_data.bot_token
    )
    await dump_statuses_every_n_sec(my_user_id,  60)


if __name__ == '__main__':
    asyncio.run(main())
