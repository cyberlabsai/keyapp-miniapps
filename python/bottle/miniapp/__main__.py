#!/bin/env python3

from bottle import run

from . import settings
from . import app  # NOQA:F401


run(host='0.0.0.0', port=settings.PORT)
