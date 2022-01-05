import configparser

from telethon import TelegramClient

from parser import telethon_data, dump_status

config = configparser.ConfigParser()

config.read("config.ini")

# Присваиваем значения внутренним переменным
telethon_data["phone"] = config['Telegram']['phone']
telethon_data["api_id"] = config['Telegram']['api_id']
telethon_data["api_hash"] = config['Telegram']['api_hash']
telethon_data["username"] = config['Telegram']['username']

links = ["mofeytea",
         "mothersterrorist",
         "kukuruzka_7",
         "ksenono",
         "deniskilseev"]


def main():
    parse(links)


def parse(links):
    telethon_data["client"] = TelegramClient(
        telethon_data["username"],
        int(telethon_data["api_id"]),
        telethon_data["api_hash"]
    )
    telethon_data["client"].start()
    for link in links:
        user = telethon_data["client"].get_entity("https://t.me/" + link)
        print(link, dump_status(user))


main()