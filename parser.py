from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest


class TelethonData:
    client: str = None
    api_id: int = 0
    api_hash: str = None
    username: str = None
    phone: str = None
    bot_token: str = "5021843702:AAE6_Jsdan2nW0AT3__lUhAKvegNICl6S90"

    code: str = None


telethon_data = TelethonData()


async def dump_status(client, user) -> str:
    print(user)
    user_info = client(GetFullUserRequest(user))
    print(user_info)
    status = user_info
    if status is None:
        status = ""
    return status
