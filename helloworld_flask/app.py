from flask import Flask

def create_app(config_filename=''):
    # create a minimal app
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)

    # simple hello world view
    @app.route('/')
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/hello/<username>') # dynamic route
    def hello_user(username):
        return 'Why Hello %s!\n' % username

    return app