# Perceptron com Seleção de Atributos usando Hill Climbing

Este script aplica o algoritmo **Perceptron** sobre o conjunto de dados "Breast Cancer Wisconsin" do repositório UCI, realizando uma **seleção de atributos** com o método de busca **Hill Climbing**.

## 📚 Conteúdos abordados

- Carregamento de dados com `ucimlrepo`
- Pré-processamento de dados (conversão de rótulos e normalização básica)
- Implementação do algoritmo Perceptron do zero
- Avaliação com acurácia
- Seleção de atributos com Hill Climbing

## 📊 Sobre o Dataset

O dataset contém informações sobre características extraídas de imagens digitalizadas de células do tecido mamário. Cada amostra é rotulada como:

- M (Maligno) → 1
- B (Benigno) → 0
- E possui 30 atributos numéricos (como raio, textura, perímetro, área, etc).
- O dataset é carregado diretamente da biblioteca ucimlrepo.

## 🔁 Como rodar

### Requisitos

Você precisa ter instalado:

- Python 3.8+
- `ucimlrepo`

Instale com:

```bash
pip install ucimlrepo
```

## 📄 Sobre o Código

Este projeto implementa um modelo de Perceptron para classificar dados do conjunto Breast Cancer Wisconsin (Diagnostic), disponível no repositório da UCI Machine Learning. Nele é aplicado o código do algoritmo de Hill Climbing para realizar a seleção de atributos que maximizem a acurácia do modelo.

### 🔍 Explicação do Funcionamento

- 1. Carregamento do dataset

  - Usa a função fetch_ucirepo(id=17) para obter os dados do câncer de mama.

- 2. Pré-processamento

  - Os rótulos M e B são convertidos em 1 e 0.
  - O DataFrame é convertido em listas para facilitar os cálculos manuais.

- 3. Divisão treino/teste

  - Os dados são embaralhados e divididos (70% treino, 30% teste).

- 4. Treinamento do Perceptron

  - Inicializa pesos com 0
  - Atualiza pesos a cada amostra, durante várias épocas
  - Usa função de ativação degrau

- 5. Hill Climbing para seleção de atributos

  - Começa com nenhum atributo selecionado
  - A cada iteração, tenta adicionar o atributo que mais aumenta a acurácia
  - Para quando não há mais melhorias

### ▶️ Ordem de Execução

```bash
⬇️ Importações
⬇️ Carrega e prepara os dados
⬇️ Converte X e y
⬇️ Divide treino e teste
⬇️ Define funções (ainda não executa)
⬇️ Executa Hill Climbing (treina e testa modelos com diferentes atributos)
⬇️ Imprime os resultados
```

### 🐍 Funções em Python utilizadas

- `zip()`: Agrupa elementos de duas listas, elemento a elemento.
- `sum()`: Soma os elementos de um iterável.
- `random.shuffle()`: Embaralha os dados para a divisão treino/teste.
- `list comprehension`: Usada extensivamente para criar subconjuntos de atributos.

### 🧮 Exemplo de Saída

```bash
Atributos Selecionados: [27, 0, 7]
Melhor Acurácia: 0.9473684210526315
```

## 📚 Possíveis Expansões

Substituir Perceptron por MLP (Multi-layer Perceptron)

Usar outras métricas: F1-score, matriz de confusão

Implementar outros métodos de seleção de atributos (RFE, Random Search)

## 👨‍💻 Autor

Desenvolvido por [Saul Basso Junior]
