from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, DecimalField, SubmitField, SelectField, FileField, HiddenField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Email
import decimal

class RegisterForm(FlaskForm):
    name = StringField(
        validators = [DataRequired()]
    )
    email = StringField(
        validators = [Email(), DataRequired()]
    )
    password = PasswordField(
        validators=[ DataRequired()]
    )
    role = HiddenField(
        default='wanner'
    )
    submit = SubmitField()

class LoginForm(FlaskForm):

    email = StringField(
        validators = [Email(), DataRequired()]
    )
    password = PasswordField(
        validators=[ DataRequired()]
    )
    submit = SubmitField()


class ProductForm(FlaskForm):
    title = StringField(
        validators = [DataRequired()]
    )
    description = StringField(
        validators = [DataRequired()]
    )
    photo_file = FileField()
    price = DecimalField(
        places = 2, 
        rounding = decimal.ROUND_HALF_UP, 
        validators = [DataRequired(), NumberRange(min = 0)]
    )
    category_id = SelectField(
        validators = [InputRequired()]
    )
    submit = SubmitField()

# Formulari generic per esborrar i aprofitar la CSRF Protection
class DeleteForm(FlaskForm):
    submit = SubmitField()

class BanForm(FlaskForm):
    reason = StringField(
        validators = [DataRequired()]
    )
    submit = SubmitField()

class UnbanForm(FlaskForm):
    submit = SubmitField()

class BlockUserForm(FlaskForm):
    user_id = HiddenField(
        validators=[DataRequired()]
    )
    message = StringField(
        validators=[DataRequired()]
    )
    submit = SubmitField()