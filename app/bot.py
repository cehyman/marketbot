import os

import discord
from dotenv import load_dotenv
import steammarket as sm
from datetime import datetime


load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_MARKET_CHANNEL_ID'))

client = discord.Client(intents=discord.Intents.default())
mp5 = sm.get_csgo_item('StatTrak™ MP5-SD | Phosphor (Factory New)', currency='USD')['volume']
ump45 = sm.get_csgo_item('StatTrak™ UMP-45 | Momentum (Factory New)', currency='USD')['volume']
deagle = sm.get_csgo_item('StatTrak™ Desert Eagle | Mecha Industries (Factory New)', currency='USD')['volume']
now = datetime.now()
current_time = now.strftime("%H:%M:%S")     
date = datetime.date(now)     
  
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(CHANNEL_ID)

    await channel.send(f'The current time and date is {current_time} on {date}\n    - Volume for StatTrak™ MP5-SD | Phosphor (Factory New): {mp5}\n- Volume for StatTrak™ UMP-45 | Momentum (Factory New): {ump45}\n- Volume for StatTrak™ Desert Eagle | Mecha Industries (Factory New): {deagle}')
        
client.run(TOKEN)