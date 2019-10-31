# import modules
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# init app Flask
app = Flask(__name__)
app.config.from_object(Config)
# init database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import app functional
from my_app import routes, models