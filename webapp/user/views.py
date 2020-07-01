from flask import Blueprint,render_template,flash,url_for
from flask_login import login_user, current_user, logout_user
from werkzeug.utils import redirect
from webapp.user.models import User
from webapp.user.forms import Login_form,Reg_form
from webapp.db import db

blueprint = Blueprint('users',__name__,url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Autorization'
    form = Login_form()
    return render_template('user/login.html', title=title, form=form)

@blueprint.route("/process-login", methods=['POST'])
def process_login():
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user,remember=form.remember_me.data)
            flash('You come')
            return redirect(url_for('news.index'))
    flash('incorrect password')
    return redirect(url_for('users.login'))

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You logout')
    return redirect(url_for('news.index'))

@blueprint.route('/reg')
def reg():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Registration'
    form = Reg_form()
    return render_template('user/reg.html', title=title, form=form)

@blueprint.route("/process-reg", methods=['POST'])
def process_reg():
    form = Reg_form()
    if form.validate_on_submit():

        new_user = User(username = form.username.data, email = form.email.data,role = 'user',is_active = True)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегались')
        return redirect(url_for('users.login'))
    else:
        for field,errors in form.errors.items():
            for error in errors:
                flash('ошибка в поле"{}":{}'.format(getattr(form,field).label.text,error))
                redirect(url_for('users.reg'))
    flash('Форма невалидна, исправте')
    return redirect(url_for('users.reg'))