from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models import Salary, Goal
from app.extensions import db
from .services import calcular_salario, progresso_meta

salary_bp = Blueprint('salary', __name__)

@salary_bp.route("/", methods=["GET", "POST"])
@login_required
def salary():
    resultado = None
    metas = None
    salario_atual = Salary.query.filter_by(user_id=current_user.id).first()

    if request.method == "POST":
        bruto = float(request.form["bruto"])
        resultado = calcular_salario(bruto)

        if salario_atual:
            salario_atual.bruto = resultado["bruto"]
            salario_atual.liquido = resultado["liquido"]
        else:
            salario_atual = Salary(
                user_id=current_user.id,
                bruto=resultado["bruto"],
                liquido=resultado["liquido"]
            )
            db.session.add(salario_atual)

        db.session.commit()

    # Calcular progresso das metas
    metas_query = Goal.query.filter_by(user_id=current_user.id).all()
    metas = []
    for m in metas_query:
        m.progresso = progresso_meta(m)
        metas.append(m)

    return render_template("salary/index.html", resultado=resultado, metas=metas, salario_atual=salario_atual)


@salary_bp.route("/edit-salary", methods=["GET", "POST"])
@login_required
def edit_salary():
    salario_atual = Salary.query.filter_by(user_id=current_user.id).first_or_404()

    if request.method == "POST":
        bruto = float(request.form["bruto"])
        resultado = calcular_salario(bruto)

        salario_atual.bruto = resultado["bruto"]
        salario_atual.liquido = resultado["liquido"]
        db.session.commit()

        return redirect(url_for("salary.salary"))

    return render_template("salary/edit_salary.html", salario=salario_atual)

@salary_bp.route("/add-goal", methods=["GET", "POST"])
@login_required
def add_goal():
    if request.method == "POST":
        nome = request.form["nome"]
        valor_objetivo = float(request.form["valor_objetivo"])
        valor_atual = float(request.form.get("valor_atual", 0))

        goal = Goal(
            user_id=current_user.id,
            nome=nome,
            valor_objetivo=valor_objetivo,
            valor_atual=valor_atual
        )
        db.session.add(goal)
        db.session.commit()

        return redirect(url_for("salary.goals"))

    return render_template("salary/add_goal.html")

@salary_bp.route("/edit-goal/<int:goal_id>", methods=["GET", "POST"])
@login_required
def edit_goal(goal_id):
    goal = Goal.query.filter_by(id=goal_id, user_id=current_user.id).first_or_404()

    if request.method == "POST":
        valor_atual = float(request.form["valor_atual"])

        goal.valor_atual = valor_atual
        db.session.commit()

        return redirect(url_for("salary.goals"))

    progresso = (goal.valor_atual / goal.valor_objetivo) * 100 if goal.valor_objetivo > 0 else 0
    restante = goal.valor_objetivo - goal.valor_atual

    return render_template("salary/edit_goal.html", goal=goal, progresso=round(progresso, 1), restante=round(restante, 2))

@salary_bp.route("/goals")
@login_required
def goals():
    goals = Goal.query.filter_by(user_id=current_user.id).all()
    goals_com_progresso = []
    for goal in goals:
        progresso = (goal.valor_atual / goal.valor_objetivo) * 100 if goal.valor_objetivo > 0 else 0
        goal.progresso = progresso
        goals_com_progresso.append(goal)

    return render_template("salary/goals.html", goals=goals_com_progresso)