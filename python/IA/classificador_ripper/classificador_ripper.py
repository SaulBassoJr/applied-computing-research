import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.impute import SimpleImputer
import wittgenstein as lw
from ucimlrepo import fetch_ucirepo

# Definir a configuração global
pd.set_option('future.no_silent_downcasting', True)

# Carregamento dos dados
congressional_voting_records = fetch_ucirepo(id=105)
X = congressional_voting_records.data.features
y = congressional_voting_records.data.targets.squeeze()

# Imputação de valores ausentes
imputer = SimpleImputer(strategy='most_frequent')
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Pré-processamento
X_imputed = X_imputed.replace({'y': 1, 'n': 0, '?': np.nan})
X_imputed = X_imputed.infer_objects(copy=False)
X_imputed = X_imputed.dropna().copy()
y = y.loc[X_imputed.index].copy()
y = y.map({'democrat': 0, 'republican': 1})

# Divisão dos dados
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.3)

# Combinação de X e y para o formato esperado pelo wittgenstein
train_data = X_train.copy()
train_data['party'] = y_train
test_data = X_test.copy()
test_data['party'] = y_test

# Parâmetros para o Hill Climbing
best_accuracy = 0
best_k = None
best_prune_size = None

# Intervalos de valores para k e prune_size
k_values = range(1, 6)
prune_sizes = [0.1, 0.2, 0.3, 0.4, 0.5]

# Hill Climbing para encontrar os melhores hiperparâmetros
for k in k_values:
    for prune_size in prune_sizes:
        clf = lw.RIPPER(k=k, prune_size=prune_size)
        clf.fit(train_data, class_feat='party')
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
            best_prune_size = prune_size
            best_model = clf  # Salvar o melhor modelo

# Treinamento final com os melhores hiperparâmetros
final_clf = lw.RIPPER(k=best_k, prune_size=best_prune_size)
final_clf.fit(train_data, class_feat='party')

# Avaliação do modelo
final_predictions = final_clf.predict(X_test)
final_accuracy = accuracy_score(y_test, final_predictions)
final_precision = precision_score(y_test, final_predictions)
final_recall = recall_score(y_test, final_predictions)
final_f1 = f1_score(y_test, final_predictions)

print(f'\nMelhor acurácia: {final_accuracy:.4f}')
print(f'Precisão: {final_precision:.4f}')
print(f'Recall: {final_recall:.4f}')
print(f'F1-score: {final_f1:.4f}')
print(f'Melhores hiperparâmetros K: {best_k},  prune_size: {best_prune_size} \n')

# Quantidade de previsões feitas para cada classe
unique, counts = np.unique(final_predictions, return_counts=True)
pred_counts = dict(zip(unique, counts))
print(f"Previsões feitas pelo modelo:")
print(f"Democratas previstos: {pred_counts.get(0, 0)}")
print(f"Republicanos previstos: {pred_counts.get(1, 0)} \n")


# Exibe regras aprendidas
raw_rules = str(final_clf.ruleset_)
clean_rules = raw_rules.strip("[]")  # remove os colchetes externos
rule_list = clean_rules.split("] V [")  # separa as regras

# Determinar a classe positiva
classe_positiva = final_clf.pos_class
nome_classe = 'Republicano' if classe_positiva == 1 else 'Democrata'

# Imprime regras aprendidas
print(f"Regras aprendidas (aplicam-se à classe: {nome_classe}):")
for i, rule in enumerate(rule_list, 1):
    conditions = rule.replace("[", "").replace("]", "").split("^")
    formatted = " E ".join(conditions)
    print(f"Regra {i}: SE {formatted} ENTÃO classe = {nome_classe}")

print("\n")