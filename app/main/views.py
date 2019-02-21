from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User,Role
from .forms import PostForm,CommentForm,UpdateProfile,SubscribeForm
from .. import db
from flask_login import login_user, logout_user, login_required, current_user
import datetime

from ..email import mail_message

@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome Lyrified'
    form = PostForm()
   
    return render_template('index.html', form=form)

@main.route('/user/<uname>')
def account(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



