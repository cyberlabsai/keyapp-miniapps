import bottle

from . import settings


def render(template_name, **context):
    return bottle.template(
        f"templates/{template_name}",
        BASE_PATH=settings.BASE_PATH,
        **context,
    )
