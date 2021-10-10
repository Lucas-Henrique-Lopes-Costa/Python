import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

url = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"
dataUsuarios = pd.read_csv(url)
# print(dataUsuarios)

# dependendo de quais os sites que a pessoa acessa, para que pessoa é mais eficiênte que eu mostre o chat para contato?

x =  dataUsuarios[["home", "how_it_works", "contact"]] # páginas que ele acess
y = dataUsuarios[["bought"]] # se o usuário comprou
# print(dataUsuarios)

modelo = LinearSVC()
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y)

modelo.fit(treino_x, treino_y.values.ravel())

previsoes = modelo.predict(teste_x)
accuracy = accuracy_score(teste_y, previsoes) * 100

print(f'Previsões: {previsoes}')
print(f'Taxa de acerto: {accuracy}')