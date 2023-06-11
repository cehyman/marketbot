from steampy.client import SteamClient
from dotenv import load_dotenv
import os

load_dotenv()
STEAM_API_KEY = os.getenv('STEAM_API_KEY')
STEAM_USERNAME = os.getenv('STEAM_USERNAME')
STEAM_PASSWORD = os.getenv('STEAM_PASSWORD')


steam_client = SteamClient(STEAM_API_KEY)
steam_client.login(STEAM_USERNAME, STEAM_PASSWORD, 'PATH_TO_STEAMGUARD_FILE')
steam_client.logout()