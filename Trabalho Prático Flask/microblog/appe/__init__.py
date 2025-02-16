
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


appo = Flask(__name__)

login = LoginManager(appo)
appo.config["SECRET_KEY"] = 'julhaea'

appo.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///microblog.db"

db = SQLAlchemy()
db.init_app(appo)

from appe import routes, alquimias
from appe.models import models
with appo.app_context():
    db.create_all()

if __name__ == "__main__":
    appo.run(debug=True)
 