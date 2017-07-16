from flask import Flask, Blueprint
from .views.controller import main
import os

root_path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, root_path=root_path)

# Register the blueprints
app.register_blueprint(main)
