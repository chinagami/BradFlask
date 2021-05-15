from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, Form
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Length(min=1,max=50)])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')