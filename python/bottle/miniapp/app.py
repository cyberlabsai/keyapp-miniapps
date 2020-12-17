import bottle

from . import http
from . import miniapp  # NOQA
from . import templates

# TODO: enable CORs (maybe?)
# from . import cors
# bottle.add_hook('after_request')(cors.add_cors_headers)


@bottle.route('/')
def root():
    token = bottle.request.query.get('token', None)
    if token is not None:
        return http.redirect(f"miniapp?token={token}")

    return templates.render("root.html")
