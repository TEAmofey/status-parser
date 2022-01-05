import json
# для корректного переноса времени сообщений в json
from datetime import datetime

from telethon.sync import TelegramClient
# класс для работы с сообщениями
from telethon.tl.functions.users import GetFullUserRequest

telethon_data = {
    "client": None,
    "api_id": None,
    "api_hash": None,
    "username": None,
    "phone": None,

    # Тип str обязателен
    "code": None
}


def dump_status(user):
    client: TelegramClient = telethon_data["client"]
    info = client(GetFullUserRequest(user))
    return info.about
