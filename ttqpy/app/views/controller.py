from flask import Blueprint, jsonify
import flask as flask

main = Blueprint('main', __name__)

@main.route('/home')
@main.route('/index')
@main.route('/')
def hello_world():
    """GET to generate a list of endpoints and their docstrings"""
    urls = dict([(r.rule, str(r))
                 for r in flask.current_app.url_map.iter_rules()
                 if not r.rule.startswith('/static')])
    return flask.render_template('index.html', urls=urls)
