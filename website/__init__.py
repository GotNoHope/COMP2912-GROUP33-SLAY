from flask import Flask

def create_web():
    web = Flask(__name__)

    from .views import main
    web.register_blueprint(main)

    # from .auth import auth
    # web.register_blueprint(auth, url_prefix='/auth')

    return web
