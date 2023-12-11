from flask import Flask, Blueprint, render_template, redirect, url_for, flash, current_app
from flask_login import current_user, login_user, login_required, logout_user
from . import db_manager as db
from . import login_manager
from .models import User, BlockedUser
from .forms import LoginForm, RegisterForm
from .helper_role import notify_identity_changed
from . import mail_manager
from werkzeug.security import generate_password_hash, check_password_hash
import secrets


auth_bp = Blueprint(
    'auth_bp', __name__, template_folder="templates", static_folder="static"
)

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        current_app.logger.debug('User already in session, redirecting')
        return redirect(url_for("main_bp.init"))

    form =  LoginForm()

    if form.validate_on_submit():
        current_app.logger.debug('Logging user...')
        email = form.email.data
        password_plain = form.password.data

        user = load_user(email)
        if user and check_password_hash(user.password, password_plain):
            login_user(user)
            notify_identity_changed()
            current_app.logger.debug('Log-in successful!')
            flash("Benvingut a Wannapop!","success")
            return redirect(url_for('main_bp.init'))
        else:
            current_app.logger.debug('Log-in error, check credentials for errors')
            flash("Comprova que els credencials siguin correctes!","warning")
            return redirect(url_for('auth_bp.login'))
    
    return render_template('auth/login.html', form = form)

@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        current_app.logger.debug('User already in session, redirecting')
        return redirect(url_for("main_bp.init"))

    form =  RegisterForm()

    if form.validate_on_submit():
        current_app.logger.debug('Registering new user...')
        name = form.name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        role = 'wanner'
        email_token  = secrets.token_urlsafe(20)
        verified = 0
        
        new_user = User(name=name, email=email, password=password, role=role, email_token=email_token, verified=verified)
        current_app.logger.debug(f"DADES DE L'USUARI: {new_user.name, new_user.email, new_user.password, new_user.role, new_user.email_token, new_user.verified}")
        db.session.add(new_user)

        # verification_url = f"/verify/{name}/{email_token}"
        # message = f"Benvingut/da a Wannapop! Entra al següent enllaç per verificar el teu compte: {verification_url}"
        # mail_manager.send_contact_msg(message)

        try:
            db.session.commit()
            current_app.logger.debug('User registered to DB, check mail to verify')
            flash("Nou compte creat! Ja pots entrar dins de Wannapop.","success")
            return redirect(url_for('main_bp.init'))
        except:
           db.session.rollback()
           current_app.logger.debug('Register error, DB changes rolled back')
           flash("Error en la creació del compte.","error")


    return render_template('auth/register.html', form = form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))

@auth_bp.route("/profile")
@login_required
def profile():
    blocked_user = BlockedUser.query.filter_by(user_id=current_user.id).first()
    return render_template("auth/profile.html", blocked_user = blocked_user)

@login_manager.user_loader
def load_user(email):
    if email is not None:
        current_app.logger.debug('Checking for user \"'+email+'\"...')
        user_exists = db.session.query(User).filter(User.email == email).one_or_none()
        return user_exists
    return None

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_bp.login"))