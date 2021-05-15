from flask import (Blueprint, render_template)
from data import Articles

bp = Blueprint('articles', __name__)

Articles = Articles()

@bp.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@bp.route('/articles/<int:id>')
def post(id):
    return render_template('post.html', article = Articles, id=id-1)