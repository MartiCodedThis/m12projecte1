from . import db_manager as db
from sqlalchemy.sql import func
from flask_login import UserMixin
from .mixins import BaseMixin, SerializableMixin

class Product(db.Model, BaseMixin, SerializableMixin):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    photo = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("users.id")) #db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created = db.Column(db.DateTime, server_default=func.now())
    updated = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Category(db.Model, BaseMixin, SerializableMixin):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)

class User(db.Model, BaseMixin, SerializableMixin, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable = False)
    email_token = db.Column(db.String)
    verified = db.Column(db.Integer)

    exclude_attr = ['password']
    
    def get_id(self):
        return self.email
    
class BlockedUser(db.Model, BaseMixin, SerializableMixin):
    __tablename__ = "blocked_users"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    message = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, server_default=func.now())

class BannedProduct(db.Model, BaseMixin, SerializableMixin):
    __tablename__ = "banned_products"
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    reason = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, server_default=func.now())

class Order(db.Model, BaseMixin, SerializableMixin):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    offer = db.Column(db.Money)
    created = db.Column(db.DateTime)

class ConfirmedOrder(db.Model, BaseMixin, SerializableMixin):
    __tablename__ = "confirmed_orders"
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    created = db.Column(db.DateTime)