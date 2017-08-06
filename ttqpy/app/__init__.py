from flask import Flask, g

from ttqpy.app.views.controller import main
from ttqpy.db import db
from ttqpy.app.config import Config
from ttqpy.app.views.api import answer_types_api, user_api, login_api
import os
import logging
from flask_mail import Mail

root_path = os.path.dirname(os.path.abspath(__file__))
app = Flask("TTQPY", root_path=root_path)



# Register the blueprints
app.register_blueprint(main)
app.register_blueprint(user_api)
app.register_blueprint(answer_types_api)
app.register_blueprint(login_api)

# Configure
app.logger.setLevel(logging.DEBUG)
app.config.from_object(Config())
db.init_app(app)
mail = Mail(app)
app.mail = mail

if __name__ == "__main__":
    app.run()
