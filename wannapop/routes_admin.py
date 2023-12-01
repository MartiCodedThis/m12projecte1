from flask import Blueprint, render_template, current_app
from flask_login import current_user, login_required
from .models import User, Product
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
    current_app.logger.debug('Loading user list...')
    users = db.session.query(User).all()
    return render_template('users_list.html', users=users)

@admin_bp.route('/admin/products')
@login_required
@require_admin_role.require(http_exception=403)
def admin_products():
    current_app.logger.debug('Loading product list...')
    products = db.session.query(Product).all()
    return render_template('products_list.html', products=products)

@admin_bp.route('/admin/products/<int:product_id>/ban')
@login_required
@require_admin_role.require(http_exception=403)
def ban_product(product_id):
    return 