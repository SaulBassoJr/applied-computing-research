import random
from ucimlrepo import fetch_ucirepo

# Fetch dataset
breast_cancer = fetch_ucirepo(id=17)
X = breast_cancer.data.features
y = breast_cancer.data.targets

# Conversão de rótulos de string para int (M = 1, B = 0)
y = y.iloc[:, 0].map({'M': 1, 'B': 0}).tolist()

# Converte DataFrame para lista de listas
X = X.values.tolist()

# Número de atributos
n_features = len(X[0])

# Função para dividir os dados em treino e teste
def train_test_split(X, y, test_size=0.3):
    data = list(zip(X, y))
    random.shuffle(data) # Embaralha os dados de maneira diferente antes de serem divididos em treino e teste
    X, y = zip(*data)
    split_idx = int(len(X) * (1 - test_size))
    return list(X[:split_idx]), list(X[split_idx:]), list(y[:split_idx]), list(y[split_idx:])

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Perceptron
def perceptron_train(X, y, epochs=1000, learning_rate=0.1):
    weights = [0.0] * (len(X[0]) + 1)
    for _ in range(epochs):
        for xi, target in zip(X, y):
            activation = weights[0] + sum(w * x for w, x in zip(weights[1:], xi))
            prediction = 1 if activation >= 0 else 0
            error = target - prediction
            weights[0] += learning_rate * error
            for i in range(len(xi)):
                weights[i + 1] += learning_rate * error * xi[i]
    return weights

#Prevê um valor de saída para uma linha dado um conjunto de pesos.
def perceptron_predict(X, weights):
    predictions = []
    for xi in X:
        activation = weights[0] + sum(w * x for w, x in zip(weights[1:], xi))
        predictions.append(1 if activation >= 0 else 0)
    return predictions

def accuracy_score(y_true, y_pred):
    correct = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp)
    return correct / len(y_true)

# Hill Climbing para seleção de atributos
selected_features = []
best_score = 0

for _ in range(n_features):
    best_candidate = None
    for i in range(n_features):
        if i not in selected_features: # Para cada atributo i que ainda não foi escolhido, testa se ele melhora o desempenho do modelo
            candidate_features = selected_features + [i] # Cria a lista de atributos
            X_train_sel = [[x[j] for j in candidate_features] for x in X_train] # Filtra as features para usar somente as do subconjunto candidato
            X_test_sel = [[x[j] for j in candidate_features] for x in X_test]   # Filtra as features //
            weights = perceptron_train(X_train_sel, y_train) # Treina o Perceptron com os dados reduzidos
            y_pred = perceptron_predict(X_test_sel, weights) # Faz previsões 
            score = accuracy_score(y_test, y_pred)  # Calcula a acurácia
            if score > best_score: # Compara e Guarda o melhor candidato 
                best_score = score 
                best_candidate = i
    if best_candidate is not None: # Se algum atributo novo melhorou o modelo, ele é adicionado à lista final
        selected_features.append(best_candidate)
    else:
        break

# Resultados
print("Atributos Selecionados:", selected_features)
print("Melhor Acurácia:", best_score)