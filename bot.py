from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# loading the token
load_dotenv()
token: Final = os.getenv('discord_token')
print(token)

# setting up the bot
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

# overall messaging functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Messages were empty - probably because intents were disabled?')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as e:
        print(e)

# startup handling
@client.event
async def on_ready() -> None:
    print(f'{client.user} running lesssgoooooooooo')

# message handling
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'{username} in {channel} said: {user_message}')
    await send_message(message, user_message)

# main entry point
def main() -> None:
    client.run(token=token)

if __name__ == '__main__':
    main()