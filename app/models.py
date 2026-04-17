from .extensions import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))

class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    bruto = db.Column(db.Float)
    liquido = db.Column(db.Float)

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    valor = db.Column(db.Float)
    categoria = db.Column(db.String(50))

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    valor = db.Column(db.Float)
    categoria = db.Column(db.String(50))
    descricao = db.Column(db.String(200))
    data = db.Column(db.Date, default=datetime.utcnow)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    nome = db.Column(db.String(100))
    valor_objetivo = db.Column(db.Float)
    valor_atual = db.Column(db.Float, default=0)