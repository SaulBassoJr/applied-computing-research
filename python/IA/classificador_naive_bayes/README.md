# Classificador Naive Bayes com Seleção de Atributos usando Hill Climbing

Este script aplica o classificador **Naive Bayes** sobre o conjunto de dados "Congressional Voting Records" do repositório UCI, realizando uma **seleção de atributos** com o método de busca **Hill Climbing**.

## 📚 Conteúdos abordados

- Carregamento de dados com `ucimlrepo`
- Pré-processamento de dados (conversão de valores categóricos e imputação)
- Treinamento e avaliação de um classificador Naive Bayes
- Seleção de atributos com Hill Climbing

## 📊 Sobre o classificador Naive Bayes (NB)

É um dos algoritmos de aprendizado supervisionado mais simples e amplamente utilizados, baseado no Teorema de Bayes com a suposição de independência condicional entre as características.

### Teorema de Bayes

O Teorema de Bayes é a base matemática por trás do classificador Naive Bayes. Ele descreve a probabilidade de um evento A ocorrer, dado que o evento B ocorreu, usando as probabilidades condicionais. A fórmula é:

​Onde:

- P(A|B) é a probabilidade de A dado B.
- P(B|A) é a probabilidade de B dado A.
- P(A) é a probabilidade a priori de A.
- P(B) é a probabilidade a priori de B.

No contexto do Naive Bayes, estamos interessados em calcular a probabilidade de uma classe 𝐶 dada as características 𝑋1,𝑋2,...,𝑋𝑛 (onde 𝑋i são os atributos ou características de entrada), ou seja, 𝑃(𝐶∣𝑋1,𝑋2,...,𝑋𝑛)

### Tipos de Classificadores Naive Bayes

Existem diferentes variações do Naive Bayes, dependendo da natureza dos dados de entrada. Os mais comuns são:

1. Gaussian Naive Bayes (GaussianNB):

   - Usado quando as características (atributos) são contínuas e seguem uma distribuição normal (gaussiana).
   - Para cada classe, é estimada a média e a variância das características, e essas informações são usadas para calcular a probabilidade de cada característica dada a classe.

2. Multinomial Naive Bayes (MultinomialNB):

   - Usado quando as características representam contagens de eventos discretos (por exemplo, frequência de palavras em texto).
   - É muito utilizado em problemas de classificação de texto (como spam vs não spam).

3. Bernoulli Naive Bayes (BernoulliNB):
   - Usado quando as características são binárias (ex: presença ou ausência de uma palavra em um texto, 1 ou 0).
   - Similar ao MultinomialNB, mas assume que cada característica é uma variável binária.

### Como o Naive Bayes Funciona na Prática

1. Treinamento (Fase de Ajuste):

   - O modelo é treinado com um conjunto de dados rotulados (com as classes já conhecidas).
   - Durante o treinamento, para cada classe, o modelo calcula:
     - A probabilidade a priori da classe 𝑃(𝐶).
     - A probabilidade condicional de cada característica dado a classe 𝑃(𝑋𝑖∣𝐶).
   - As probabilidades 𝑃(𝐶) e 𝑃(𝑋𝑖∣𝐶) podem ser calculadas a partir das frequências observadas nos dados de treinamento.

2. Predição (Fase de Inferência):
   - Quando o modelo é aplicado a dados de teste, ele calcula as probabilidades 𝑃(𝐶∣𝑋1,𝑋2,...,𝑋𝑛) para cada classe possível 𝐶, e escolhe a classe com a maior probabilidade.
   - A previsão é dada pela classe 𝐶 que maximiza a expressão de Bayes.

## 📊 Sobre o Dataset

O dataset contém os registros de votação de 435 membros da Câmara dos Representantes dos EUA em 1984. Cada amostra indica o voto de um congressista em 16 propostas legislativas, com os seguintes valores:

- `y` → Votou sim (convertido para 1)
- `n` → Votou não (convertido para 0)
- `?` → Ausente ou voto desconhecido (convertido para `NaN`, tratado com imputação)

As classes são:

- **republican**
- **democrat**

O dataset é carregado diretamente da biblioteca `ucimlrepo`.

## 🔁 Como rodar

### Requisitos

Você precisa ter instalado:

- Python 3.8+
- `scikit-learn`
- `pandas`
- `ucimlrepo`

Instale com:

```bash
pip install scikit-learn
```

```bash
pip install pandas
```

```bash
pip install ucimlrepo
```

## 📄 Sobre o Código

Este projeto implementa um classificador Naive Bayes para prever a filiação partidária de membros do congresso com base em seus votos em diferentes projetos de lei. A seleção de atributos é feita utilizando o algoritmo Hill Climbing, que busca maximizar a acurácia da classificação.

### 🔍 Explicação do Funcionamento

1. Carregamento do dataset

- Usa `fetch_ucirepo(id=105)` para obter os dados do Congressional Voting Records.

2. Pré-processamento

   - Os valores 'y', 'n' e '?' são convertidos para 1, 0 e `NaN`, respectivamente.
   - Os valores ausentes são substituídos pela moda (valor mais frequente) da coluna.

3. Divisão treino/teste

   - Os dados são divididos aleatoriamente em 70% para treino e 30% para teste.

4. Treinamento do Naive Bayes

   - Utiliza `GaussianNB` da biblioteca `scikit-learn`.

5. Hill Climbing para seleção de atributos
   - Começa com nenhum atributo selecionado
   - A cada iteração, adiciona o atributo que mais aumenta a acurácia
   - Para quando não há mais melhorias

### ▶️ Ordem de Execução

```bash
⬇️ Importações
⬇️ Carrega e prepara os dados
⬇️ Converte valores categóricos e trata os ausentes
⬇️ Divide treino e teste
⬇️ Executa Hill Climbing (treina e testa modelos com diferentes atributos)
⬇️ Imprime os resultados
```

### 🐍 Funções em Python utilizadas

- `replace()`: Substitui valores categóricos por numéricos.
- `SimpleImputer`: Substitui valores ausentes pela moda.
- `train_test_split()`: Divide os dados em treino e teste.
- `GaussianNB()`: Implementa o classificador Naive Bayes.
- `accuracy_score()`: Mede a acurácia da classificação.
- `list comprehension`: Usada para selecionar subconjuntos de atributos.

### 🧮 Exemplo de Saída

```bash
Atributos Selecionados: [3]
Melhor Acurácia: 0.9694656488549618
```

## 📚 Possíveis Expansões

Usar outros classificadores: Decision Tree, KNN, SVM

Avaliar com métricas adicionais: F1-score, matriz de confusão

Comparar diferentes técnicas de seleção de atributos: RFE, Random Search

## 👨‍💻 Autor

Desenvolvido por [Saul Basso Junior]
