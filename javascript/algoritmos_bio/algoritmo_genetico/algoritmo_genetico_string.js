const TAMANHO_POPULACAO = 100;
const TAXA_MUTACAO = 0.1;
const ALVO = "PARALELEPIPEDO";

// Função para calcular a aptidão de um indivíduo
function avaliarAptidao(individuo) {
  let aptidao = 0;
  for (let i = 0; i < ALVO.length; i++) {
    if (individuo[i] === ALVO[i]) {
      aptidao++;
    }
  }
  return aptidao;
}

// Gera um indivíduo aleatório
function gerarIndividuo() {
  const letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  return Array.from(
    { length: ALVO.length },
    () => letras[Math.floor(Math.random() * letras.length)]
  ).join("");
}

// Aplica mutação em um indivíduo
function mutar(individuo) {
  const letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  return individuo
    .split("")
    .map((letra) =>
      Math.random() < TAXA_MUTACAO
        ? letras[Math.floor(Math.random() * letras.length)]
        : letra
    )
    .join("");
}

// Realiza o crossover entre dois pais
function crossover(pai, mae) {
  const pontoCorte = Math.floor(Math.random() * pai.length);
  return pai.slice(0, pontoCorte) + mae.slice(pontoCorte);
}

// Inicializa a população
let populacao = Array.from({ length: TAMANHO_POPULACAO }, gerarIndividuo);
let geracao = 0;

// Loop evolutivo
while (true) {
  geracao++;

  // Avaliação da aptidão e ordenação da população
  populacao.sort((a, b) => avaliarAptidao(b) - avaliarAptidao(a));
  const melhorIndividuo = populacao[0];
  const melhorAptidao = avaliarAptidao(melhorIndividuo);

  console.log(
    `Geração ${geracao}: ${melhorIndividuo} | Aptidão: ${melhorAptidao}`
  );

  // Verifica se encontrou a solução
  if (melhorAptidao === ALVO.length) {
    console.log(`Solução encontrada na geração ${geracao}!`);
    break;
  }

  // Cria a nova população
  const novaPopulacao = [];

  for (let i = 0; i < TAMANHO_POPULACAO; i++) {
    const pai = populacao[Math.floor(Math.random() * 5)]; // Seleção dos melhores
    const mae = populacao[Math.floor(Math.random() * 5)];
    let filho = crossover(pai, mae);
    filho = mutar(filho);
    novaPopulacao.push(filho);
  }

  populacao = novaPopulacao;
}
