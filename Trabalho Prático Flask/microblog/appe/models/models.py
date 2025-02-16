from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from appe import db
from flask_login import UserMixin
from appe import login

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    remember: Mapped[bool] = mapped_column(default=False)
    foto_perfil: Mapped[str] = mapped_column(nullable=True)  # Novo campo
    last_login: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    bio: Mapped[str] = mapped_column(nullable=True)

    # Relacionamento com Nota
    notas: Mapped[list['Nota']] = relationship(back_populates='author')

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class Nota(db.Model):
    __tablename__ = 'notas'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    conteudo: Mapped[str] = mapped_column(nullable=False)
    time: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'))

    # Relacionamento com User
    author: Mapped[User] = relationship(back_populates='notas')