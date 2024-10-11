from browser import document

def calcular_rescisao_acordo(event):
    event.preventDefault()  # Previne o envio padrão do formulário

    try:
        salario = float(document['salario'].value)
        dias_trabalhados = int(document['dias_trabalhados'].value)
        meses_trabalhados = int(document['meses_trabalhados'].value)
        fgts = float(document['fgts'].value)

        # Calcular o saldo de salário
        diaria = salario / 30
        saldo_salario = diaria * dias_trabalhados

        # Calcular o aviso-prévio
        aviso_previo_diarias = min(90, dias_trabalhados * 3)
        valor_aviso_previo = diaria * aviso_previo_diarias
        aviso_previo = valor_aviso_previo / 2  # 50% do aviso-prévio

        # Calcular 13º salário proporcional
        decimo_terceiro = (salario / 12) * meses_trabalhados

        # Calcular férias
        ferias_integral = salario + (salario / 3)
        ferias_proporcionais = (salario / 12) * meses_trabalhados
        ferias_proporcionais += (ferias_proporcionais / 3)  # Incluindo 1/3 de férias

        # Calcular FGTS e multa de 20%
        fgts_devido = salario * 0.08 * (meses_trabalhados)
        multa_fgts = fgts_devido * 0.20

        # Total da rescisão
        total_rescisao = saldo_salario + aviso_previo + decimo_terceiro + ferias_integral + ferias_proporcionais + multa_fgts

        # Exibir resultados
        document['resultados'].innerHTML = f"""
        <h2>Resultados:</h2>
        <p>Saldo de Salário: R$ {saldo_salario:.2f}</p>
        <p>Aviso Prévio (50%): R$ {aviso_previo:.2f}</p>
        <p>13º Salário Proporcional: R$ {decimo_terceiro:.2f}</p>
        <p>Férias Integrais: R$ {ferias_integral:.2f}</p>
        <p>Férias Proporcionais: R$ {ferias_proporcionais:.2f}</p>
        <p>Multa de 20% sobre FGTS: R$ {multa_fgts:.2f}</p>
        <p><strong>Total da Rescisão: R$ {total_rescisao:.2f}</strong></p>
        """
    except ValueError:
        document['resultados'].innerHTML = "<p>Por favor, insira valores válidos.</p>"

document['formulario'].bind('submit', calcular_rescisao_acordo)
