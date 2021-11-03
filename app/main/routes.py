from . import main
from flask import render_template
from flask_login import current_user

@main.route('/home')
def home():

    return render_template('main/home_1.html',
                                            user = current_user)