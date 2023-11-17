from flask import Blueprint, render_template, redirect, url_for, flash
from . import db_manager as db
from . import login_manager

from .models import User

from .forms import LoginForm


auth_bp = Blueprint(
    'auth_bp', __name__, template_folder="templates", static_folder="static"
)

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    form =  LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        plain_text_password = form.password.data

        if email is not None:
            user_exists = db.session.query(User).filter(User.email == email).one_or_none()
            
            if user_exists: 
                flash("Benvingut a Wannapop!","success")
                return redirect(url_for('main_bp.product_list'))
            else:
                flash("Error autenticant usuari","error")
                return redirect(url_for('auth_bp.login'))
    
    return render_template('auth/login.html', form = form)