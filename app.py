# myapp/__init__.py

from main_app.controllers.users import users_bp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
cors = CORS(app)


app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(debug=True)
