from flask import Blueprint, render_template, current_app, flash, redirect, url_for
from flask_login import current_user, login_required
from .models import User, Product, BannedProduct
from .forms import BanForm, UnbanForm
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
    for product in products:
        banned = db.session.query(BannedProduct).filter(BannedProduct.product_id == product.id).first()
        product.banned = banned is not None
    return render_template('products_list.html', products=products)

@admin_bp.route('/admin/products/<int:product_id>/ban', methods = ['GET', 'POST'])
@login_required
@require_admin_role.require(http_exception=403)
def ban_product(product_id):
    product = db.session.query(Product).filter(Product.id == product_id).one()

    form = BanForm()

    if form.validate_on_submit(): # si s'ha fet submit al formulari
        current_app.logger.debug('Banning product...')

        ban = BannedProduct()
        ban.product_id = product_id
        ban.reason = form.reason.data
        db.session.add(ban)
        db.session.commit()

        current_app.logger.debug('Product banned successfuly! Redirecting')
        return redirect(url_for('admin_bp.admin_products'))
    return render_template('ban_product.html', product=product, form=form)

@admin_bp.route('/admin/products/<int:product_id>/unban', methods = ['GET', 'POST'])
@login_required
@require_admin_role.require(http_exception=403)
def unban_product(product_id):
    product = db.session.query(Product).filter(Product.id == product_id).one()
    ban = db.session.query(BannedProduct).filter(BannedProduct.product_id == product_id).one()
    form = UnbanForm()

    if form.validate_on_submit(): # si s'ha fet submit al formulari
        current_app.logger.debug('Unbanning product...')
        
        db.session.delete(ban)
        db.session.commit()

        current_app.logger.debug('Product unbanned successfuly! Redirecting')
        return redirect(url_for('admin_bp.admin_products'))

    return render_template('unban_product.html', product=product, form=form)