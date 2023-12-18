# controllers/users.py

from flask import Blueprint, render_template
from main_app.models.user import User

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/')
def index():
    users = User.query.all()
    return render_template('users/index.html', users=users)
