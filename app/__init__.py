from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app import config
from module_dotenv import secret_key


app = Flask(__name__)
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=config.POSTGRES_URI)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import views
