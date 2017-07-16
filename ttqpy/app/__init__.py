from flask import Flask, Blueprint
from .views.controller import main
import os

root_path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, root_path=root_path)

# Register the blueprints
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
