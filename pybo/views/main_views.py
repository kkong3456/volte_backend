from flask import Blueprint, redirect,render_template, url_for
from pybo.models import Question

bp=Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello,Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
