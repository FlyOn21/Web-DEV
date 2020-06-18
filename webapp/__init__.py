from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import locale
from webapp.model import News, db, User
from webapp.weather import weather_city
from datetime import datetime
from webapp.form import Login_form


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def lode_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        title = "Новости Python"
        locale.setlocale(locale.LC_ALL, "ru")
        news_list = News.query.order_by(News.published.desc()).all()
        weather_c = weather_city(app.config['WEATHER_DEFAULT_CITY'])
        if weather_c == False:
            return "Sorry,something went wrong"
        else:
            city_now = weather_c[0]["query"]
            weather_now = weather_c[1]["temp_C"]
            date = datetime.now().strftime('%a %d/%m/%Y')
        return render_template('index.html', page_title=title, city=city_now, weather_c=weather_now, date=date,
                               news_list=news_list)

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Autorization'
        login_form = Login_form()
        return render_template('login.html', title=title, login_form=login_form)

    @app.route("/process-login", methods=['POST'])
    def process_login():
        form = Login_form()
        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('You come')
                return redirect(url_for('index'))
        flash('incorrect password')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('You logout')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_1():
        if current_user.is_admin:
            return 'Admin'
        else:
            return 'Not admin'



    return app
