from flask import Flask, render_template, redirect
from data.users import User
from forms.register import RegisterForm

from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.run()


@app.route("/register", methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('login.html', title='Регистрация',
                                   form=form)

        db_sess = db_session.create_session()

        user = User(surname=form.surname.data, name=form.name.data, age=form.age.data,
                    position=form.position.data, speciality=form.speciality.data, address=form.address.data,
                    email=form.email.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/done',)
    return render_template('login.html', title='Регистрация', form=form)


@app.route("/done")
def done():
    return 'ОК'


if __name__ == '__main__':
    main()
