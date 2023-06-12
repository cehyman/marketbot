
import discord
import steammarket as sm
from datetime import datetime

from config.config import Config
cfg = Config()

client = discord.Client(intents=discord.Intents.default())
   
  
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(cfg.discord_market_channel_id)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")     
    date = datetime.date(now)  

    await channel.send(f'The current time and date is {current_time} on {date}')
        
client.run(cfg.discord_bot_token)