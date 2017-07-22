from flask import Blueprint, render_template, abort, g
from jinja2 import TemplateNotFound
from ttqpy.db import db

main = Blueprint('main', __name__)

@main.route('/home')
@main.route('/index')
@main.route('/')
def hello_world():
    return 'Hello, World! {}'.format(db.__dict__)
