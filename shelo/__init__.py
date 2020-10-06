# import modules
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# init app Flask
app = Flask(__name__)
app.config.from_object(Config)
# init database
db = SQLAlchemy(app)

# import app functional
from shelo import routes, models