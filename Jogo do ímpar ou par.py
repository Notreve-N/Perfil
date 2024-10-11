from browser import document, window

def runGame(event):
    event.preventDefault()  # Prevenir o comportamento padrão do formulário
    escolha = document["escolha"].value
    numero_usuario = int(document["numero"].value)
    numero_computador = window.Math.floor(window.Math.random() * 11)  # Gera um número entre 0 e 10
    soma = numero_usuario + numero_computador
    resultado = "Par" if soma % 2 == 0 else "Ímpar"

    mensagem = f"Você escolheu: {escolha}<br>"
    mensagem += f"Seu número: {numero_usuario}<br>"
    mensagem += f"Número do computador: {numero_computador}<br>"
    mensagem += f"Soma: {soma}<br>"
    mensagem += f"Resultado: {resultado}<br>"
    
    if escolha.lower() == resultado.lower():
        mensagem += "Você ganhou!"
    else:
        mensagem += "Você perdeu!"

    document["resultados"].innerHTML = mensagem
    document["novoJogo"].style.display = "inline-block"  # Mostrar o botão "Novo Jogo"
    document["jogar"].style.display = "none"  # Esconder o botão "Jogar"

def novoJogo(event):
    document["escolha"].value = "par"  # Redefinir o campo de escolha para "par"
    document["numero"].value = ""  # Limpar o campo de número
    document["resultados"].innerHTML = ""  # Limpar os resultados
    document["novoJogo"].style.display = "none"  # Esconder o botão "Novo Jogo"
    document["jogar"].style.display = "inline-block"  # Mostrar o botão "Jogar"

document["formulario"].bind("submit", runGame)
document["novoJogo"].bind("click", novoJogo)
