from browser import document

def calcular_rescisao(event):
    event.preventDefault()  # Previne o envio padrão do formulário

    try:
        salario = float(document['salario'].value)
        anos = int(document['anos'].value)
        meses = int(document['meses'].value)
        fgts = float(document['fgts'].value)

        # Calcular o aviso prévio
        aviso_previo = min(90, anos * 3)  # 3 dias por ano de trabalho, até um máximo de 90 dias
        valor_aviso_previo = (salario / 30) * aviso_previo

        # Calcular férias vencidas
        ferias_vencidas = salario + (salario / 3)

        # Calcular férias proporcionais
        ferias_proporcionais = (salario / 12) * meses

        # Calcular 13º salário proporcional
        decimo_terceiro = (salario / 12) * meses

        # Calcular FGTS (Multa de 40% sobre o saldo de FGTS)
        fgts_rescisao = fgts * 0.4

        # Calcular o total da rescisão
        total_rescisao = valor_aviso_previo + ferias_vencidas + ferias_proporcionais + decimo_terceiro + fgts_rescisao

        # Exibir resultados
        document['resultados'].innerHTML = f"""
        <h2>Resultados:</h2>
        <p>Aviso Prévio: R$ {valor_aviso_previo:.2f}</p>
        <p>Férias Vencidas: R$ {ferias_vencidas:.2f}</p>
        <p>Férias Proporcionais: R$ {ferias_proporcionais:.2f}</p>
        <p>13º Salário Proporcional: R$ {decimo_terceiro:.2f}</p>
        <p>FGTS (Multa de 40%): R$ {fgts_rescisao:.2f}</p>
        <p><strong>Total da Rescisão: R$ {total_rescisao:.2f}</strong></p>
        """
    except ValueError:
        document['resultados'].innerHTML = "<p>Por favor, insira valores válidos.</p>"

document['formulario'].bind('submit', calcular_rescisao)