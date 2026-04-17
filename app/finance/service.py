from collections import defaultdict


def gerar_fatura(salario, despesas):
    total_gastos = sum(d.valor for d in despesas)

    gastos_por_categoria = defaultdict(float)

    for d in despesas:
        gastos_por_categoria[d.categoria] += d.valor

    saldo = salario - total_gastos

    percentual_gasto = (total_gastos / salario) * 100 if salario > 0 else 0

    return {
        "salario": salario,
        "total_gastos": round(total_gastos, 2),
        "saldo": round(saldo, 2),
        "percentual_gasto": round(percentual_gasto, 2),
        "gastos_por_categoria": dict(gastos_por_categoria)
    }


def gerar_insights(fatura):
    insights = []

    if fatura["percentual_gasto"] > 90:
        insights.append("⚠️ Você está gastando mais de 90% do seu salário.")

    return insights


def calcular_score(fatura):
    score = 100

    percentual = fatura["percentual_gasto"]
    saldo = fatura["saldo"]

    # penalizações
    if percentual > 100:
        score -= 40
    elif percentual > 90:
        score -= 25
    elif percentual > 75:
        score -= 15

    if saldo < 0:
        score -= 30

    # bônus
    if percentual < 50:
        score += 10

    # limitar entre 0 e 100
    score = max(min(score, 100), 0)

    return score

def classificar_score(score):
    if score >= 80:
        return "Excelente 🟢"
    elif score >= 60:
        return "Bom 🟡"
    elif score >= 40:
        return "Atenção 🟠"
    else:
        return "Crítico 🔴"
    

def evolucao_mensal(despesas, salario):
    meses = defaultdict(lambda: {"gastos": 0, "salario": salario})

    for d in despesas:
        mes = d.data.strftime("%Y-%m")
        meses[mes]["gastos"] += d.valor

    resultado = []

    for mes in sorted(meses.keys()):
        gastos = meses[mes]["gastos"]
        sal = meses[mes]["salario"]
        saldo = sal - gastos

        resultado.append({
            "mes": mes,
            "gastos": round(gastos, 2),
            "salario": sal,
            "saldo": round(saldo, 2)
        })

    return resultado
