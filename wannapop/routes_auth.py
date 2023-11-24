from flask import Flask, Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from . import db_manager as db
from . import login_manager

from .models import User
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

@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.init"))

    form =  RegisterForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        role = 'wanner'
        email_token  = secrets.token_urlsafe(20)
        verified = 0
        
        new_user = User(name=name, email=email, password=password, role=role, email_token=email_token, verified=verified)
        print(f"DADES DE L'USUARI: {new_user.name, new_user.email, new_user.password, new_user.role, new_user.email_token, new_user.verified}")
        db.session.add(new_user)

        verification_url = f"/verify/{name}/{email_token}"
        message = f"Benvingut/da a Wannapop! Entra al següent enllaç per verificar el teu compte: {verification_url}"
        mail_manager.send_contact_msg(message)

        try:
            db.session.commit()
            flash("Nou compte creat! Ja pots entrar dins de Wannapop.","success")
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

@auth_bp.route("/profile")
@login_required
def profile():
    
    return render_template("auth/profile.html")

@login_manager.user_loader
def load_user(email):
    if email is not None:
        user_exists = db.session.query(User).filter(User.email == email).one_or_none()
        return user_exists
    return None

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_bp.login"))