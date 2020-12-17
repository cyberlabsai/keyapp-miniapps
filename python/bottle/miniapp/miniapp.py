import bottle

from . import http
from . import key
# from . import settings
from . import templates


@bottle.route('/miniapp')
def root():
    token = bottle.request.query.get('token', None)

    if token is None:
        user_data = None
        ex = "Você deve acessar esta página somente por meio da KeyApp"
    else:
        try:
            user_data = key.exchange_token_for_user_data(token)
        except Exception as e:
            user_data = None
            ex = e

    if user_data is None:
        return bottle.template(
            "templates/miniapp/unauthorized.html",
            {
                "exception": ex
            }
        )

    return templates.render(
        "miniapp/root.html",
        user_data=user_data,
    )
