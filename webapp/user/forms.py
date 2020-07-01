from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, HiddenField,BooleanField
from wtforms.validators import DataRequired,EqualTo,Email,ValidationError
from webapp.user.models import User
from sqlalchemy.exc import IntegrityError


class Login_form(FlaskForm):
    username = StringField('User name', validators=[DataRequired()],render_kw={'class':"form-control"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={'class':"form-control"})
    hidden_f = HiddenField()
    remember_me = BooleanField('Запомни меня', default=True, render_kw= {'class':"form-check-input"})
    submit = SubmitField('SEND',render_kw={"class":"btn btn-primary"})


class Reg_form(FlaskForm):
    username = StringField('User name', validators=[DataRequired()],render_kw={'class':"form-control"})
    email  = StringField('Email', validators=[DataRequired(),Email()],render_kw={'class':"form-control"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={'class':"form-control"})
    password_2 = PasswordField('Password', validators=[DataRequired(),EqualTo('password')],render_kw={'class':"form-control"})
    hidden_f = HiddenField()
    submit = SubmitField('SEND',render_kw={"class":"btn btn-primary"})

    def validate_username(self,username):
        user_c = User.query.filter_by(username = username.data).count()
        if user_c > 0:
            raise ValidationError('Пользователь с таким логином сушествует')

    def validate_mail(self, email):
        user_mail = User.query.filter_by(email = email.data).count()
        if  user_mail > 0:
            raise ValidationError('Пользователь с таким мылом сушествует')

