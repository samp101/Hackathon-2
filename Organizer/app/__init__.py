import flask
import flask_sqlalchemy
import flask_migrate
from config import Config


app = flask.Flask(__name__)
app.config.from_object(Config)

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app,db)



from app import routes, models
