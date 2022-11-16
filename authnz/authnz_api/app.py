import os
from werkzeug.contrib.fixers import ProxyFix

from api import create_app


app = create_app()


def run():
    debug = os.environ.get('APP_DEBUG', False)
    host = os.environ.get('LISTEN_ADDRESS')
    port = int(os.environ.get('LISTEN_PORT'))

    app.run(debug=debug, host=host, port=port)


wsgi = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    run()
