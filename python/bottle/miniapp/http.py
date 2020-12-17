import bottle

from . import settings


def redirect(path):
    response = bottle.response
    response.status = 302
    location = f"{settings.BASE_PATH}/{path}"
    response.set_header("Location", location)
    return response
