from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
#sets up db to be an sqlite db and will set up a file, local not external db
db = SQLAlchemy(app)

from application import routes