import bottle


def add_cors_headers(response=None):
    response = response or bottle.response

    the_headers = response.headers

    the_headers['Access-Control-Allow-Origin'] = '*'
    the_headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    the_headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
