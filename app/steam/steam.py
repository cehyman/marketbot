from steampy.client import SteamClient
from steampy.models import GameOptions

from config.config import Config

def main():
    cfg = Config()

    steam_client = SteamClient(cfg.steam_api_key)
    steam_client.login(cfg.steam_username, cfg.steam_password, cfg.steam_guard)
    item = 'M4A1-S | Cyrex (Factory New)'
    response = steam_client.market.fetch_price_history(item, GameOptions.CS)
    print(response)

if __name__ == "__main__":
    main()