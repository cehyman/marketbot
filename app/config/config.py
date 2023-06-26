from dotenv import load_dotenv
import os

class Config():
    def __init__(self) -> None:
        
        load_dotenv()
        
        self.steam_api_key = os.getenv('STEAM_API_KEY')
        self.steam_username = os.getenv('STEAM_USERNAME')
        self.steam_password = os.getenv('STEAM_PASSWORD')
        self.steam_guard = os.getenv('STEAM_GUARD')
        
        self.discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')
        self.discord_market_channel_id = int(os.getenv('DISCORD_MARKET_CHANNEL_ID'))
        
        self.postgres_user = os.getenv('POSTGRES_USER')
        self.postgres_password = os.getenv('POSTGRES_PASSWORD')
        self.postgres_db = os.getenv('POSTGRES_DB')
        self.postgres_host = os.getenv('POSTGRES_HOST')
        self.postgres_port = os.getenv('POSTGRES_PORT')
        
        self.prefix = '!'