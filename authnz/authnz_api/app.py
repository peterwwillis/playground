import os
from werkzeug.middleware.proxy_fix import ProxyFix

from api import create_app

def run():
    debug = os.environ.get('APP_DEBUG', False)
    host = os.environ.get('LISTEN_ADDRESS')
    port = int(os.environ.get('LISTEN_PORT'))

    app = create_app()

    #app.wsgi_app = ProxyFix(
    #    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    #)

    #app.run(debug=debug, host=host, port=port)
    return app


if __name__ == '__main__':
    run()
