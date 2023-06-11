import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_GENERAL_CHANNEL_ID'))

client = discord.Client(intents=discord.Intents.default())
            
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f'Hello, I am {client.user}!')

client.run(TOKEN)