from flask import Flask
from mongoengine import connect
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)

    mongo_uri = os.getenv('MONGODB_URI')
    connect(host=mongo_uri)

    from app.routes.routes import user_bp
    app.register_blueprint(user_bp)

    @app.route("/")
    def index():
        return "Working", 200

    return app