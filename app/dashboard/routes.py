from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Expense, Salary, Goal
from app.finance.service import gerar_fatura, gerar_insights, calcular_score, classificar_score, evolucao_mensal

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
@login_required
def home():
    despesas = Expense.query.filter_by(user_id=current_user.id).all()
    salario = Salary.query.filter_by(user_id=current_user.id).first()
    metas = Goal.query.filter_by(user_id=current_user.id).all()

    fatura = None
    insights = []
    score = None
    classificacao = None
    evolucao = None

    if salario:
        fatura = gerar_fatura(salario.liquido, despesas)
        insights = gerar_insights(fatura)
        score = calcular_score(fatura)
        classificacao = classificar_score(score)
        evolucao = evolucao_mensal(despesas, salario.liquido)

    # Calcular progresso das metas
    metas_com_progresso = []
    for meta in metas:
        progresso = (meta.valor_atual / meta.valor_objetivo) * 100 if meta.valor_objetivo > 0 else 0
        metas_com_progresso.append({
            'id': meta.id,
            'nome': meta.nome,
            'valor_objetivo': meta.valor_objetivo,
            'valor_atual': meta.valor_atual,
            'progresso': round(progresso, 1)
        })

    return render_template(
        "dashboard/home.html",
        fatura=fatura,
        insights=insights,
        score=score,
        classificacao=classificacao,
        evolucao=evolucao,
        metas=metas_com_progresso
    )

@dashboard_bp.route("/reports")
@login_required
def reports():
    despesas = Expense.query.filter_by(user_id=current_user.id).all()
    salario = Salary.query.filter_by(user_id=current_user.id).first()

    fatura = None
    insights = []
    score = None
    classificacao = None
    evolucao = None
    categoria_mais_gasta = None
    valor_mais_gasto = 0

    if salario:
        fatura = gerar_fatura(salario.liquido, despesas)
        insights = gerar_insights(fatura)
        score = calcular_score(fatura)
        classificacao = classificar_score(score)
        evolucao = evolucao_mensal(despesas, salario.liquido)

        # Encontrar categoria com maior gasto
        if fatura and fatura["gastos_por_categoria"]:
            categoria_mais_gasta = max(fatura["gastos_por_categoria"], key=fatura["gastos_por_categoria"].get)
            valor_mais_gasto = fatura["gastos_por_categoria"][categoria_mais_gasta]

    return render_template(
        "dashboard/reports.html",
        fatura=fatura,
        insights=insights,
        score=score,
        classificacao=classificacao,
        evolucao=evolucao,
        categoria_mais_gasta=categoria_mais_gasta,
        valor_mais_gasto=valor_mais_gasto
    )

@dashboard_bp.route("/settings")
@login_required
def settings():
    return render_template("dashboard/settings.html")

