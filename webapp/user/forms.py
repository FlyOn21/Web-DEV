from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, HiddenField,BooleanField
from wtforms.validators import DataRequired


class Login_form(FlaskForm):
    username = StringField('User name', validators=[DataRequired()],render_kw={'class':"form-control"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={'class':"form-control"})
    hidden_f = HiddenField()
    remember_me = BooleanField('Запомни меня', default=True, render_kw= {'class':"form-check-input"})
    submit = SubmitField('SEND',render_kw={"class":"btn btn-primary"})
