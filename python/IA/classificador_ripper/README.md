# Classificador RIPPER com Ajuste de Hiperparâmetros usando Hill Climbing

Este script implementa um **classificador baseado em regras (RIPPER)** para prever a filiação partidária de membros do Congresso dos EUA, utilizando o conjunto de dados "Congressional Voting Records" do repositório UCI. O modelo passa por ajuste de hiperparâmetros via **Hill Climbing**, e exibe as regras aprendidas de forma interpretável.

## 📚 Conteúdos abordados

- Carregamento de dados com `ucimlrepo`
- Imputação e conversão de valores categóricos
- Treinamento de modelo RIPPER com a biblioteca `wittgenstein`
- Busca pelos melhores hiperparâmetros `k` e `prune_size` com Hill Climbing
- Avaliação com métricas de classificação (acurácia, precisão, recall, F1-score)
- Exibição das regras aprendidas de forma legível

## 📊 Sobre o classificador RIPPER

O RIPPER (**Repeated Incremental Pruning to Produce Error Reduction**) é um algoritmo de aprendizado supervisionado baseado em **regras de decisão**. Ele busca encontrar regras lógicas que separem bem as classes dos dados, sendo uma alternativa interpretável e eficiente em problemas de classificação.

### Como o RIPPER Funciona

RIPPER gera regras iterativamente para a classe positiva (minoritária) utilizando duas fases principais:

1. **Fase de crescimento (growing)**:

   - Regras são criadas adicionando condições que maximizam a cobertura da classe-alvo, enquanto minimizam os erros.

2. **Fase de poda (pruning)**:

   - As regras são simplificadas para melhorar a generalização, removendo partes que não contribuem significativamente.

O processo é controlado por dois hiperparâmetros principais:

- `k`: número de interações de refinamento das regras.
- `prune_size`: proporção de instâncias usadas na poda.

As regras geradas são facilmente interpretáveis e podem ser lidas como sentenças "SE... ENTÃO...".

## 📊 Sobre o Dataset

O dataset contém os registros de votação de 435 membros da Câmara dos Representantes dos EUA em 1984. Cada amostra indica o voto de um congressista em 16 propostas legislativas, com os seguintes valores:

- `y` → Votou sim (convertido para 1)
- `n` → Votou não (convertido para 0)
- `?` → Voto ausente/desconhecido (imputado pela moda)

As classes são:

- **republican (1)**
- **democrat (0)**

O dataset é carregado diretamente da biblioteca `ucimlrepo`.

## 🔁 Como rodar

### Requisitos

Você precisa ter instalado:

- Python 3.8+
- `scikit-learn`
- `pandas`
- `ucimlrepo`
- `wittgenstein`

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

```bash
pip install wittgenstein
```

## 📄 Sobre o Código

Este projeto implementa um classificador RIPPER para prever a filiação partidária de membros do congresso com base em seus votos em diferentes projetos de lei. A seleção de hiperparâmetros (`k` e `prune_size`) é feita utilizando o algoritmo Hill Climbing, que busca maximizar a acurácia da classificação.

### 🔍 Explicação do Funcionamento

1. Carregamento do dataset

- Usa `fetch_ucirepo(id=105)` para obter os dados do Congressional Voting Records.

2. Pré-processamento

   - Os valores 'y', 'n' e '?' são convertidos para 1, 0 e `NaN`, respectivamente.
   - Os valores ausentes são substituídos pela moda (valor mais frequente) da coluna.

3. Divisão treino/teste

   - Os dados são divididos aleatoriamente em 70% para treino e 30% para teste.

4. Hill Climbing para seleção de atributos

   - Testa diferentes combinações de k e prune_size
   - Avalia a acurácia para cada combinação
   - Seleciona o melhor modelo encontrado

5. Extração de Regra

   - As regras aprendidas são exibidas de forma interpretável, no estilo:
     - **SE** condição1 **E** cindição2 **ENTÂO** classe = Republicano

### ▶️ Ordem de Execução

```bash
⬇️ Importações
⬇️ Carrega e prepara os dados
⬇️ Converte valores categóricos e trata os ausentes
⬇️ Divide treino e teste
⬇️ Executa Hill Climbing (testa diferentes hiperparâmetros)
⬇️ Treina o melhor modelo encontrado
⬇️ Imprime as métricas e as regras
```

### 🐍 Funções em Python utilizadas

- `replace()`: Substitui valores categóricos por numéricos.
- `SimpleImputer`: Substitui valores ausentes pela moda.
- `train_test_split()`: Divide os dados em treino e teste.
- `RIPPER()`: Algoritmo baseado em regras da biblioteca `wittgenstein`.
- `accuracy_score()`, `precision_score()`, `recall_score()`, `f1_score()`: Métricas de avaliação.
- `out_model()` e `ruleset_`: Extraem as regras aprendidas.

### 🧮 Exemplo de Saída

```bash
Melhor acurácia: 0.9542
Precisão: 1.0000
Recall: 0.8696
F1-score: 0.9302
Melhores hiperparâmetros K: 2,  prune_size: 0.2

Previsões feitas pelo modelo:
Democratas previstos: 91
Republicanos previstos: 40

Regras aprendidas (aplicam-se à classe: Republicano):
Regra 1: SE physician-fee-freeze=1 E education-spending=1 ENTÃO classe = Republicano
Regra 2: SE physician-fee-freeze=1 ENTÃO classe = Republicano
```

## 📚 Possíveis Expansões

Usar validação cruzada para avaliação mais robusta

Adicionar outras métricas: ROC AUC, matriz de confusão

Comparar com outros classificadores: Naive Bayes, Decision Tree, SVM

Exportar as regras aprendidas para arquivo `.txt` ou `.csv`

## 👨‍💻 Autor

Desenvolvido por [Saul Basso Junior]
