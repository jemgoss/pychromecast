"""
Data and methods to retrieve app specific configuration
"""

import json
from typing import cast

from urllib.request import urlopen

APP_BACKDROP = "E8C28D3C"
APP_YOUTUBE = "233637DE"
APP_MEDIA_RECEIVER = "CC1AD845"
APP_PLEX = "06ee44ee-e7e3-4249-83b6-f5d0b6f07f34_1"
APP_DASHCAST = "84912283"
APP_HOMEASSISTANT_LOVELACE = "A078F6B0"
APP_HOMEASSISTANT_MEDIA = "B45F4572"
APP_SUPLA = "A41B766D"
APP_YLEAREENA = "A9BCCB7C"
APP_BUBBLEUPNP = "3927FA74"
APP_BBCSOUNDS = "D350F6A9"
APP_BBCIPLAYER = "5E81F6DB"
APP_SHAKA = "07AEE832"
APP_NRKTV = "3AEDF8D1"
APP_NRKRADIO = "A49874B1"
APP_AUDIBLE = "25456794"


def get_possible_app_ids() -> list[str]:
    """ Returns all possible app ids. """

    try:
        with urlopen("https://clients3.google.com/cast/chromecast/device/baseconfig") as response:
            response.read(4)
            data = json.load(response)
        return cast(
            list[str],
            [app["app_id"] for app in data["applications"]] + data["enabled_app_ids"],
        )

    except ValueError:
        # If json fails to parse
        return []


def get_app_config(app_id: str) -> dict:
    """ Get specific configuration for 'app_id'. """
    try:
        with urlopen(f"https://clients3.google.com/cast/chromecast/device/app?a={app_id}") as response:
            if response.status == 200:
                response.read(4)
                return cast(dict, json.load(response))
            return {}

    except ValueError:
        # If json fails to parse
        return {}
