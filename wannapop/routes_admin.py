from flask import Blueprint, render_template, current_app
from flask_login import current_user, login_required
from .models import User, BlockedUser
from .forms import BlockUserForm
from .helper_role import require_admin_moderator, require_admin_role
from . import db_manager as db

# Blueprint
admin_bp = Blueprint(
    "admin_bp", __name__, template_folder="templates/admin", static_folder="static"
)

@admin_bp.route('/admin')
@login_required
@require_admin_moderator.require(http_exception=403)
def admin_index():
    return render_template('index.html')

@admin_bp.route('/admin/users')
@login_required
@require_admin_role.require(http_exception=403)
def admin_users():
    form = BlockUserForm()
        
    blocked_users = BlockedUser.query.all()
    users = db.session.query(User).all()

    return render_template('users_list.html', users=users, form=form, blocked_users = blocked_users)

@admin_bp.route('/admin/users/<int:user_id>/block', methods=['POST'])
@login_required
@require_admin_role.require(http_exception=403)
def admin_block(user_id):
    form = BlockUserForm()
    
    if form.validate_on_submit(): 
        target_user = db.session.query(User).get(user_id)
        if target_user:
            message = form.message.data
            blocked_user = BlockedUser(user_id=user_id, message=message)
            db.session.add(blocked_user)
            db.session.commit()

    
    blocked_users = BlockedUser.query.all()
    users = db.session.query(User).all()
    return render_template('users_list.html', users=users, form=form,blocked_users = blocked_users )

@admin_bp.route('/admin/users/<int:user_id>/unblock', methods=['POST'])
@login_required
@require_admin_role.require(http_exception=403)
def admin_unblock(user_id):
    form = BlockUserForm()
    target_user = db.session.query(User).get(user_id)
    if target_user:
        blocked_user = BlockedUser.query.filter_by(user_id=user_id).first()
        if blocked_user:
            db.session.delete(blocked_user)
            db.session.commit()

    users = db.session.query(User).all()
    return render_template('users_list.html', users=users, form=form)