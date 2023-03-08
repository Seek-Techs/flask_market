from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.model import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter(User.username==username_to_check.data).first()
        if user:
            raise ValidationError('username already exists! Please try a different User Name')
        
        
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter(User.email_address==email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')
    
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=3), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
    
class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()] )
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
    
class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')
    
class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')
        
    