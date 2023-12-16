from flask import Flask

from chronormu.blueprints.health.view import health


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(health, url_prefix="/health")

    return app


if __name__ == "__main__":
    server = create_app()

    server.run(host="127.0.0.1", port=5001, debug=True)
