from getpass import getpass # ВВод пароля из командной строки
import sys
from webapp import create_app
from webapp.db import db,User

app = create_app()
with app.app_context():
    username = input('input login')
    if User.query.filter(User.username ==username).count():
        print('User is exist')
        sys.exit(0)
    password_1 = getpass('Input password')
    password_2 = getpass('Confirm password')

    if not password_1 == password_2:
        print('password is not confirm')
        sys.exit(0)
    new_user = User(username = username, role = 'admin',is_active=True)
    new_user.set_password(password_1)

    db.session.add(new_user)
    db.session.commit()
    print(f'Creature new user {username}')
