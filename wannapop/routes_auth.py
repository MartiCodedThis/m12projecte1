from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from . import db_manager as db
from . import login_manager
from .models import User
from .forms import LoginForm


auth_bp = Blueprint(
    'auth_bp', __name__, template_folder="templates", static_folder="static"
)

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.init"))

    form =  LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password_plain = form.password.data

        user = load_user(email)
        if user:
            login_user(user)
            flash("Benvingut a Wannapop!","success")
            return redirect(url_for('main_bp.init'))
        else:
            flash("Error autenticant usuari","error")
            return redirect(url_for('auth_bp.login'))
    
    return render_template('auth/login.html', form = form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))

@login_manager.user_loader
def load_user(email):
    if email is not None:
        user_exists = db.session.query(User).filter(User.email == email).one_or_none()
        return user_exists
    return None

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_bp.login"))