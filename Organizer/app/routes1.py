import flask

from app import app, db
from app.forms import Form, Register, Login
from app.models import User, Todo


user_main = []


@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def login():
    login_form = Login()

    user_list = [name.name for name in User.query.all()]

    if login_form.validate_on_submit():
        name = login_form.name.data
        password = login_form.password.data
        user = User.query.filter_by(name=name).first()
        user_main.append(user)

        if name not in user_list:
            return flask.redirect('/register')

        return flask.redirect(f'/form/{user.user_id}')

    return flask.render_template('login.html', form=login_form )

@app.route('/register', methods=['GET','POST'])
def register():
    register_form = Register()
    user_list = User.query.all()

    if register_form.validate_on_submit():
        name = register_form.name.data
        last_name = register_form.last_name.data
        email = register_form.email.data
        password = register_form.password.data

        user = User(name=name, last_name=last_name, email=email,password=password)

        db.session.add(user)
        db.session.commit()

        return flask.redirect('/form')

    return flask.render_template('register.html', form=register_form, d = user_list)


@app.route('/form/<id>', methods=['GET','POST'])
def todo(id):
    form = Form()
    to_do_list_total = [errand for errand in Todo.query.filter_boy(user_id=user_main[0].user_id)]

    if form.validate_on_submit():
        todo = form.todo.data

        to_do_list = Todo(details=todo, user=user_main[0])
        db.session.add(to_do_list)
        db.session.commit()

        return flask.redirect('/form/<id>')


    return flask.render_template('form.html',form=form,list = to_do_list_total,id =id)


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete_person(id):
    p = Todo.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return flask.redirect('/form')

@app.route('/delete', methods=['GET', 'POST'])
def delete_all():
    Todo.query.delete()
    db.session.commit()
    return flask.redirect('/form')

@app.route('/completed/<id>', methods=['GET', 'POST'])
def completed(id):
    p = Todo.query.filter_by(id=id).first()
    p.completed = True if p.completed == False else False
    db.session.add(p)
    db.session.commit()
    return flask.redirect('/form')

