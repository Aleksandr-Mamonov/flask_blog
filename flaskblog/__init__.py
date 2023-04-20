import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("FLASK_SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"  # 'login' - is a function name of login route
login_manager.login_message_category = "info"

# Mail config
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_USER")
# need to use app-specific password from gmail, not real password
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASSWD")

mail = Mail(app)

from flaskblog import routes
