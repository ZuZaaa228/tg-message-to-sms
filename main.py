import asyncio
import os
import re

from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest, GetFullChannelRequest
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError
from twilio.rest import Client

load_dotenv()


def get_file_data(mask: str, filepath: str) -> list[str]:
    with open(filepath, 'r', encoding="UTF-8") as f:
        return list(map(lambda x: mask + x, f.read().split()))


# Telegram my.telegram.org
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")

# Twilio www.twilio.com
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TARGET_PHONE_NUMBER = os.getenv("TARGET_PHONE_NUMBER")

client = TelegramClient('anon', API_ID, API_HASH)

PUBLIC_CHANNEL_PATH = "chats.txt"
PUBLIC_CHANNEL_MASK = "@"
chats = get_file_data(PUBLIC_CHANNEL_MASK, PUBLIC_CHANNEL_PATH)
print(chats)

PRIVATE_CHANNEL_PATH = "invite_links.txt"
PRIVATE_CHANNEL_MASK = "https://t.me/"
invite_links = get_file_data(PRIVATE_CHANNEL_MASK, PRIVATE_CHANNEL_PATH)
print(invite_links)


def send_sms(phone_number: str, message: str):
    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    twilio_client.messages.create(
        to=phone_number,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )


def clean_and_transliterate_message(message: str) -> str:
    message = re.sub(r'[^\x00-\x7Fа-яА-Я]+', '', message)

    if len(message) > 150:
        message = message[:147] + '...'

    # Транслитерация сообщения
    try:
        transliterated_message = translit(message, reversed=True)
    except LanguageDetectionError as e:
        print(e)
        transliterated_message = message

    if len(transliterated_message) > 150:
        transliterated_message = transliterated_message[:147] + '...'

    return transliterated_message


@client.on(events.NewMessage(chats=chats))
async def handler(event) -> None:
    message = clean_and_transliterate_message(event.message.message)
    if len(message) > 10:
        print("Transliterated Message:", message)
        send_sms(TARGET_PHONE_NUMBER, message)


async def main():
    await client.start(PHONE)
    print("Client Created")

    for link in invite_links:
        try:
            result = await client(JoinChannelRequest(link))
            print(result)
            full_channel = await client(GetFullChannelRequest(result.chats[0].id))
            channel_id = full_channel.full_chat.id
            chats.append(channel_id)
            print(f"Joined channel with ID: {channel_id}")
        except Exception as e:
            print(f"Failed to join channel: {e}")

    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
