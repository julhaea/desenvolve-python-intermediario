from datetime import datetime
from sqlalchemy import select

from appe import db
from appe.models.models import User

def validate_user_password(username, password):
    res=db.session.scalars(select(User).where(User.username == username))
    user = res.first()
    if user and user.password == password: return user
    else: return None

def user_exists(username):
    res=db.session.scalars(select(User).where(User.username == username))
    user = res.first()
    return user

def create_user(username, password, remember=False, foto_perfil=None, bio=None):
    new_user = User(
        username=username,
        password=password,
        remember=remember,
        foto_perfil=foto_perfil,  # Novo campo
        bio=bio  # Novo campo
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user