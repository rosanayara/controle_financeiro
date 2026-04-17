def calcular_inss(salario_bruto):
    faixas = [
        (1412.00, 0.075),
        (2666.68, 0.09),
        (4000.03, 0.12),
        (7786.02, 0.14)
    ]

    inss = 0
    salario_restante = salario_bruto
    limite_anterior = 0

    for limite, aliquota in faixas:
        if salario_bruto > limite:
            faixa_valor = limite - limite_anterior
        else:
            faixa_valor = salario_restante

        inss += faixa_valor * aliquota
        salario_restante -= faixa_valor
        limite_anterior = limite

        if salario_restante <= 0:
            break

    # teto do INSS
    return round(min(inss, 908.85), 2)


def calcular_irrf(base_calculo):
    faixas = [
        (2259.20, 0.0, 0),
        (2826.65, 0.075, 169.44),
        (3751.05, 0.15, 381.44),
        (4664.68, 0.225, 662.77),
        (float("inf"), 0.275, 896.00)
    ]

    for limite, aliquota, deducao in faixas:
        if base_calculo <= limite:
            irrf = (base_calculo * aliquota) - deducao
            return max(round(irrf, 2), 0)


def calcular_salario(salario_bruto):
    inss = calcular_inss(salario_bruto)

    base_irrf = salario_bruto - inss

    # regra do desconto simplificado
    base_irrf_simplificada = base_irrf - 528
    irrf_simplificado = calcular_irrf(base_irrf_simplificada)

    irrf_normal = calcular_irrf(base_irrf)

    # escolhe o menor imposto
    irrf = min(irrf_normal, irrf_simplificado)

    salario_liquido = salario_bruto - inss - irrf

    return {
        "bruto": salario_bruto,
        "inss": inss,
        "irrf": irrf,
        "liquido": round(salario_liquido, 2)
    }

def previsao_futura(fatura, meses=6):
    saldo_mensal = fatura["saldo"]

    previsao = []

    acumulado = 0

    for i in range(1, meses + 1):
        acumulado += saldo_mensal

        previsao.append({
            "mes": i,
            "valor": round(acumulado, 2)
        })

    return previsao


def progresso_meta(meta):
    percentual = (meta.valor_atual / meta.valor_objetivo) * 100

    return round(percentual, 2)