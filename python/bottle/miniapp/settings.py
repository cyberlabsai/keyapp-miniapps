from os import environ


PORT = environ["PORT"]
DOMAIN = environ.get("DOMAIN", "localhost")
BASE_PATH = environ.get("BASE_PATH", f"//{DOMAIN}:{PORT}")

KEYAPP_KEY = environ["KEYAPP_KEY"]
KEYAPP_SECRET = environ["KEYAPP_SECRET"]
KEYAPP_URL = environ["KEYAPP_URL"]
