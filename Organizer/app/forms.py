import wtforms
import flask_wtf


class Form(flask_wtf.FlaskForm):
    todo = wtforms.StringField('',[wtforms.validators.InputRequired()])
    submit = wtforms.SubmitField('Add')