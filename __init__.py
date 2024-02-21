from flask import Flask

def create_web():
    web = Flask(__name__)

    from .views import main
    web.register_blueprint(main)

    return web
