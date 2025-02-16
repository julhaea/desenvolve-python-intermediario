

from flask import render_template, request, redirect, url_for, flash
from appe import appo, db
from appe import alquimias
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required
)
from appe.models.models import Nota, User
from datetime import datetime

@appo.route("/")
def index():
    user = None
    if current_user.is_authenticated:
        user = current_user

    # Recupera todas as notas com seus autores
    notas = db.session.query(Nota, User.username).join(User).order_by(Nota.time.desc()).all()

    return render_template(
        'index.html', 
        title="Página Inicial",
        user=user,
        notas=notas
    )

@appo.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method=="POST":
        username = request.form["username"].lower()
        password = request.form["password"].lower()
        
        user=alquimias.validate_user_password(username,password)
        if user:
            flash('Login bem sucedido', "success")
            login_user(user, remember=user.remember)
            return redirect(url_for(f"index"))
        else:
            flash('Usuário ou senha inválida', "error")
            return redirect(url_for('login'))
    return render_template('login.html')

@appo.route('/cadastro', methods=['POST'])
@appo.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form["username"].lower()
        password = request.form["password"].lower()
        foto_perfil = request.form.get("foto_perfil")  # Novo campo
        bio = request.form.get("bio")  # Novo campo
        remember = False

        if alquimias.user_exists(username):
            flash('Usuário já existe', 'error')
            return redirect(url_for('cadastro'))

        user = alquimias.create_user(
            username=username,
            password=password,
            remember=remember,
            foto_perfil=foto_perfil,  # Novo campo
            bio=bio  # Novo campo
        )
        login_user(user, remember=remember)
        flash('Cadastro realizado com sucesso', 'success')
        return redirect(url_for('index'))
    
    return render_template('cadastro.html')
  
@appo.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(f'index'))

@appo.route("/cria_nota", methods=["POST"])
@login_required
def cria_nota():
    conteudo = request.form.get("conteudo_nota")
    nova_nota = Nota(
            conteudo=conteudo,
            user_id=current_user.id,
            time=datetime.utcnow())
    db.session.add(nova_nota)
    db.session.commit()
    flash('Nota adicionada com sucesso!', 'success')
    return redirect(url_for('index'))


@appo.route("/excluir_nota/<int:nota_id>", methods=["POST"])
@login_required
def excluir_nota(nota_id):
    nota = Nota.query.get_or_404(nota_id)

    db.session.delete(nota)
    db.session.commit()
    flash('Nota excluída com sucesso!', 'success')
    return redirect(url_for('index'))