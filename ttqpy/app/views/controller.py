from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main = Blueprint('main', __name__)

@main.route('/home')
@main.route('/index')
@main.route('/')
def hello_world():
    return 'Hello, World!'