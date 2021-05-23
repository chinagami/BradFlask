from flask import (Blueprint, render_template)
from data import Articles
from flask_login import login_required

bp = Blueprint('articles', __name__)

Articles = Articles()

@bp.route('/articles')
@login_required
def articles():
    return render_template('articles.html', articles = Articles)

@bp.route('/articles/<int:id>')
def post(id):
    return render_template('post.html', article = Articles, id=id-1)