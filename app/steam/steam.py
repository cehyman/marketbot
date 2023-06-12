from steampy.client import SteamClient

from config.config import Config
cfg = Config()

steam_client = SteamClient(cfg.steam_api_key)


def login():
    steam_client.login(cfg.steam_username, cfg.steam_password, 'PATH_TO_STEAMGUARD_FILE')

def logout():
    steam_client.logout()