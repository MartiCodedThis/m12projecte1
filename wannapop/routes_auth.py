from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from . import db_manager as db
from . import login_manager
from .models import User
from .forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash


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
        if user and check_password_hash(user.password, password_plain):
            login_user(user)
            flash("Benvingut a Wannapop!","success")
            return redirect(url_for('main_bp.init'))
        else:
            flash("Error d'autenticació d'usuari. Comprova que els credencials siguin correctes!","error")
            return redirect(url_for('auth_bp.login'))
    
    return render_template('auth/login.html', form = form)

@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.init"))

    form =  RegisterForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        try:
            db.session.commit()
            flash("Nou compte creat! Ja pots entrar dins de Wannapop.","error")
            return redirect(url_for('main_bp.init'))
        except:
            db.session.rollback()
            flash("Error en la creació del compte.","error")


    return render_template('auth/register.html', form = form)

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