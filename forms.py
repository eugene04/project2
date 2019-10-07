from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired , Length ,Email , EqualTo




class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=4,max=25)])
    email = StringField('email address',validators =[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('sign up')

class LoginForm(FlaskForm):
   
    email = StringField('email address',validators = [DataRequired(),Email()])
    password = PasswordField('password',validators = [DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('log in')


