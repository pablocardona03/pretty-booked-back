from flask import Flask, g as global_variables
from app.infrastructure.database.di import DatabaseDI
from app.infrastructure.database.session import close_db

class Container:
    def __init__(self):
        self.database = DatabaseDI()
        # self.users = UserContainer()
        # self.products = ProductContainer()

def create_app():
    app = Flask(__name__)

    @app.before_request
    def _build_container():
        global_variables.container = Container()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        close_db()

    @app.route("/healthcheck", methods=["GET"])
    def health():
        return {"ok": True}

    return app