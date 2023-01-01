import os
from werkzeug.middleware.proxy_fix import ProxyFix

from api import create_app


debug = os.environ.get('APP_DEBUG', False)
host = os.environ.get('LISTEN_ADDRESS')
port = int(os.environ.get('LISTEN_PORT'))

def run():
    #debug = os.environ.get('APP_DEBUG', False)
    #host = os.environ.get('LISTEN_ADDRESS')
    #port = int(os.environ.get('LISTEN_PORT'))

    app = create_app()

    #app.wsgi_app = ProxyFix(
    #    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    #)

    # gunicorn
    #app.run(debug=debug, host=host, port=port)
    #return app

    # bjoern
    import bjoern
    bjoern.run(app, host, port)


if __name__ == '__main__':
    run()

