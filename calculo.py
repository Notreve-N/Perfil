from browser import document, alert

def calcular_salario(event):
    event.preventDefault()  # Evita o recarregamento da página

    try:
        # Capturando dados do formulário
        salario_bruto = float(document['salario'].value)
        inicio_trabalho = document['inicio_trabalho'].value
        termino_trabalho = document['termino_trabalho'].value
        horas_extras = float(document['horas_extras'].value) if document['horas_extras'].value else 0
        trabalha_noite = document['trabalha_noite'].value
        adicional_noturno_perc = float(document['adicional_noturno'].value) if trabalha_noite == "sim" else 0
        dias_trabalhados = int(document['dias_trabalhados'].value)

        # Função para calcular o valor da hora
        def calcular_valor_hora(salario_bruto):
            horas_mensais = 220  # Média de 220 horas trabalhadas por mês
            return salario_bruto / horas_mensais

        valor_hora = calcular_valor_hora(salario_bruto)

        # Função para calcular horas noturnas (das 22h às 05h)
        def calcular_horas_noturnas(inicio, fim):
            inicio_h, inicio_m = map(int, inicio.split(':'))
            fim_h, fim_m = map(int, fim.split(':'))

            inicio_em_minutos = inicio_h * 60 + inicio_m
            fim_em_minutos = fim_h * 60 + fim_m

            horas_noturnas = 0

            # Se a jornada começa antes de 22h e termina depois de 22h
            if inicio_em_minutos <= 22 * 60 and fim_em_minutos > 22 * 60:
                inicio_noturno = max(inicio_em_minutos, 22 * 60)
                fim_noturno = min(fim_em_minutos, 5 * 60 + 24 * 60)  # Calcula até 5h do dia seguinte

                # Convertendo para horas e retornando valor positivo
                horas_noturnas = max(0, (fim_noturno - inicio_noturno) / 60)

            return horas_noturnas

        horas_noturnas = calcular_horas_noturnas(inicio_trabalho, termino_trabalho)
        valor_adicional_noturno_dia = horas_noturnas * valor_hora * (adicional_noturno_perc / 100)

        # Cálculo de descontos (INSS e IR)
        def calcular_desconto_inss(salario_bruto):
            if salario_bruto <= 1212.00:
                return salario_bruto * 0.075
            elif salario_bruto <= 2427.35:
                return salario_bruto * 0.09
            elif salario_bruto <= 3641.03:
                return salario_bruto * 0.12
            else:
                return salario_bruto * 0.14

        def calcular_desconto_ir(salario_bruto):
            if salario_bruto <= 1903.98:
                return 0
            elif salario_bruto <= 2826.65:
                return salario_bruto * 0.075 - 142.80
            elif salario_bruto <= 3751.05:
                return salario_bruto * 0.15 - 354.80
            else:
                return salario_bruto * 0.275 - 869.36

        desconto_inss = calcular_desconto_inss(salario_bruto)
        desconto_ir = calcular_desconto_ir(salario_bruto)

        # Cálculo final do salário diário
        salario_diario = (valor_hora * 8) + valor_adicional_noturno_dia + (horas_extras * valor_hora)
        salario_mensal = salario_diario * dias_trabalhados

        # Cálculo do salário líquido mensal
        salario_liquido_mensal = salario_mensal - desconto_inss - desconto_ir

        # Exibindo resultados no HTML
        resultados = document['resultados']
        resultados.innerHTML = f"""
            <p>Valor da Hora: R$ {valor_hora:.2f}</p>
            <p>Horas Noturnas Trabalhadas: {horas_noturnas:.2f} horas</p>
            <p>Valor do Adicional Noturno (por dia): R$ {valor_adicional_noturno_dia:.2f}</p>
            <p>Valor Total do Dia: R$ {salario_diario:.2f}</p>
            <p>Salário Mensal Presumido: R$ {salario_mensal:.2f}</p>
            <p>Salário Líquido Mensal: R$ {salario_liquido_mensal:.2f}</p>
            <p>Desconto INSS: R$ {desconto_inss:.2f}</p>
            <p>Desconto IR: R$ {desconto_ir:.2f}</p>
        """
    
    except ValueError:
        alert("Por favor, preencha todos os campos corretamente.")

# Associando a função ao botão de submit
document['formulario'].bind('submit', calcular_salario)
