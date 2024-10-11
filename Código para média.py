from browser import document, window

def calcular_media(event):
    event.preventDefault()
    aluno = document["nome"].value
    nota1 = float(document["nota1"].value)
    nota2 = float(document["nota2"].value)
    media_aprovacao = float(document["mediaAprovacao"].value)
    
    media = (nota1 + nota2) / 2
    
    if media < media_aprovacao:
        mensagem = f"Aluno: {aluno}\nMédia: {media:.2f}\nSituação: Reprovado"
    elif media_aprovacao <= media <= (media_aprovacao + 1.5):
        mensagem = f"Aluno: {aluno}\nMédia: {media:.2f}\nSituação: Aprovado na média"
    else:
        mensagem = f"Aluno: {aluno}\nMédia: {media:.2f}\nSituação: Aprovado com excelência"
    
    document["resultados"].textContent = mensagem

def limpar_dados(event):
    document["formulario"].reset()
    document["resultados"].textContent = ""

document["formulario"].bind("submit", calcular_media)
document["limpar"].bind("click", limpar_dados)
