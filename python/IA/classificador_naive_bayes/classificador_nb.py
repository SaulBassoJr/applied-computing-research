import random
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# 1. Carrega a base de dados
congressional_voting = fetch_ucirepo(id=105)
X = congressional_voting.data.features
y = congressional_voting.data.targets

# 2. Pré-processamento
# Converte os valores categóricos para numéricos
X = X.replace({'y': 1, 'n': 0, '?': None}).infer_objects(copy=False)  # Deixa '?' como NaN

# Usa SimpleImputer para substituir os NaN pela moda (valor mais frequente) de cada coluna
imputer = SimpleImputer(strategy='most_frequent')
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Converte y de DataFrame para lista
y = y.iloc[:, 0].tolist()

# 3. Divide os dados em treino e teste com embaralhamento (hold-out)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=None, shuffle=True)

# Converte DataFrame para lista de listas
X_train = X_train.values.tolist()
X_test = X_test.values.tolist()

# Número de atributos
n_features = len(X_train[0])

# 4. Hill Climbing para seleção de atributos
selected_features = []
best_score = 0

# Embaralha os atributos para evitar que o processo de seleção de atributos siga uma ordem específica
attributes = list(range(n_features))

# Embaralha a ordem dos atributos
random.shuffle(attributes)

for _ in range(n_features):
    best_candidate = None
    for i in range(n_features):
        if i not in selected_features:
            candidate_features = selected_features + [attributes[i]]
            X_train_sel = [[x[j] for j in candidate_features] for x in X_train]
            X_test_sel = [[x[j] for j in candidate_features] for x in X_test]

            # Treina o classificador Naive Bayes
            model = GaussianNB()
            model.fit(X_train_sel, y_train)
            y_pred = model.predict(X_test_sel)
            score = accuracy_score(y_test, y_pred)

            # Verifica se a acurácia melhorou
            if score > best_score:
                best_score = score
                best_candidate = attributes[i]

    if best_candidate is not None:
        selected_features.append(best_candidate)
    else:
        break

# 5. Resultados
print("Atributos Selecionados:", selected_features)
print("Melhor Acurácia:", best_score)
