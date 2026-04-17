from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user
from app.models import Expense
from app.extensions import db

finance_bp = Blueprint("finance", __name__, url_prefix="/finance")

@finance_bp.route("/add-expense", methods=["GET", "POST"])
@login_required
def add_expense():
    if request.method == "POST":
        valor = float(request.form["valor"])
        categoria = request.form["categoria"]
        descricao = request.form.get("descricao", "")

        expense = Expense(
            user_id=current_user.id,
            valor=valor,
            categoria=categoria,
            descricao=descricao
        )
        db.session.add(expense)
        db.session.commit()

        return redirect(url_for("finance.expenses"))

    return render_template("finance/add_expense.html")

@finance_bp.route("/expenses")
@login_required
def expenses():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template("finance/expenses.html", expenses=expenses)