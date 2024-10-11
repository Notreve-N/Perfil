let numeroLimite = 10;
let listaDeNumerosSorteados = [];
let numeroSecreto = gerarNumeroAleatorio();
let tentativas = 1;

exibirMensagemInicial();
document.getElementById('reiniciar').setAttribute('disabled', true); // Inicia com o botão "Novo jogo" desabilitado

function exibirTextoNaTela(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
    responsiveVoice.speak(texto, 'Brazilian Portuguese Female', { rate: 1.0 });
}

function exibirMensagemInicial() {
    exibirTextoNaTela('h1', 'Jogo do número secreto');
    exibirTextoNaTela('p', `Escolha as opções entre 1 e ${numeroLimite}`);
}

function verificarChute() {
    let chute = parseInt(document.querySelector('input').value);
    let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
    let dica;
    console.log(numeroSecreto);

    if (chute === numeroSecreto) {
        dica = '';
        exibirTextoNaTela('h1', 'Parabéns!');
        exibirTextoNaTela('p', `${dica} Você acertou o número secreto, com ${tentativas} ${palavraTentativa}`);
        document.getElementById('reiniciar').removeAttribute('disabled');
        document.getElementById('chute').setAttribute('disabled', true);
    } else {
        dica = chute > numeroSecreto ? 'O número secreto é menor <' : 'O número secreto é maior >';
        exibirTextoNaTela('h1', 'Que Pena!');
        exibirTextoNaTela('p', `${dica} Tente novamente, você teve ${tentativas} ${palavraTentativa}`);
    }
    tentativas++;
    limpaCampo();
}

function limpaCampo() {
    let campoChute = document.querySelector('input');
    campoChute.value = '';
}

function gerarNumeroAleatorio() {
    let numeroEscolhido = parseInt(Math.random() * numeroLimite + 1);
    let quantidadeDeElementosNaLista = listaDeNumerosSorteados.length;

    if (quantidadeDeElementosNaLista === numeroLimite) {
        listaDeNumerosSorteados = [];
    }

    if (listaDeNumerosSorteados.includes(numeroEscolhido)) {
        return gerarNumeroAleatorio();
    } else {
        listaDeNumerosSorteados.push(numeroEscolhido);
        console.log(listaDeNumerosSorteados);
        return numeroEscolhido;
    }
}

function reiniciarJogo() {
    exibirMensagemInicial();
    limpaCampo();
    numeroSecreto = gerarNumeroAleatorio();
    tentativas = 1;
    document.getElementById('reiniciar').setAttribute('disabled', true);
    document.getElementById('chute').removeAttribute('disabled', true);
}
