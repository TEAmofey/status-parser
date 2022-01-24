import asyncio
import configparser

from multiprocessing import Process

from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest

from bot import loop_bot
from parser import telethon_data
import logging

from time import sleep

from statuses import statuses, tostr

config = configparser.ConfigParser()

config.read("config.ini")


# Присваиваем значения внутренним переменным
telethon_data.phone = config['Telegram']['phone']
telethon_data.api_id = int(config['Telegram']['api_id'])
telethon_data.api_hash = config['Telegram']['api_hash']
telethon_data.username = config['Telegram']['username']

links = ["mofeytea",
         "mothersterrorist",
         "kukuruzka_7",
         "ksenono",
         "deniskilseev"]


def parse(client: TelegramClient, links):
    for link in links:
        user_info = client(GetFullUserRequest(link))
        status = user_info.about
        if status is None:
            status = ""
        statuses[link] = status


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def dump_statuses_every_minute():
    while True:
        telethon_data.client.connect()
        parse(telethon_data.client, links)
        # print(statuses)
        telethon_data.client.disconnect()
        sleep(3)


def loop_a():
    telethon_data.client = TelegramClient(
        telethon_data.username,
        telethon_data.api_id,
        telethon_data.api_hash
    )
    telethon_data.client.start(
        lambda: telethon_data.bot_token
    )
    telethon_data.client.disconnect()
    # client.start(
    #     lambda: telethon_data.bot_token
    # )
    dump_statuses_every_minute()


def main() -> None:
    Process(target=loop_a).start()
    Process(target=loop_bot).start()


if __name__ == '__main__':
    main()
