from flask import Flask, g
from ttqpy.app.views.controller import main
from ttqpy.db import db
import ttqpy.app.config as config

import os
import logging


root_path = os.path.dirname(os.path.abspath(__file__))
app = Flask("TTQPY", root_path=root_path)

# Register the blueprints
app.register_blueprint(main)
app.logger.setLevel(logging.DEBUG)
app.config.from_object('ttqpy.app.config')
db.init_app(app)

if __name__ == "__main__":
    app.run()
