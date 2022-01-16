import flask

from app import app, db
from app.forms import Form
from app.models import Todo



@app.route('/', methods=['GET','POST'])
@app.route('/form', methods=['GET','POST'])
def todo():
    form = Form()

    to_do_list_total = [errand for errand in Todo.query.all()]

    if form.validate_on_submit():
        todo = form.todo.data

        to_do_list = Todo(details=todo)
        db.session.add(to_do_list)
        db.session.commit()

        return flask.redirect('/form')


    return flask.render_template('form.html',form=form,list = to_do_list_total)


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

