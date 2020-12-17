import requests

from . import settings


def exchange_token_for_user_data(token):
    authorization = f"bearer {settings.KEYAPP_KEY}:{settings.KEYAPP_SECRET}"
    url = f"{settings.KEYAPP_URL}/miniapps/tokens"
    response = requests.get(
        url,
        headers={
            "Authorization": authorization,
            "token": token
        }
    )
    response.raise_for_status()
    return response.json()
