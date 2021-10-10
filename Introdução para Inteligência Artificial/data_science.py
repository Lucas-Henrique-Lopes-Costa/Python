# usando o https://movielens.org/ & conectando com o GitHub da Alura
# para isso devemos usar uma biblioteca
import pandas as pd
# pegando os filmes
url = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula2.1/movies.csv"
dataFilmes = pd.read_csv(url) # Data Frame

print('Pega apenas os 5 primeiros')
print(dataFilmes.head()) # pega apenas os 5 primeiros, só para ter uma ideia
print('')

print('Alterando o nome das colunas')
dataFilmes.columns = ['filmeId', 'título', 'gênero']
print(dataFilmes.head())
print('')

# pegando as avaliações
uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
dataNotas = pd.read_csv(uri) # Data Frame

print('Pega apenas os 5 primeiras avaliações')
print(dataNotas.head())
print('')

print('Alterando o nome das colunas')
dataNotas.columns = ["usuárioId", "filmeId", "notas", "momento"] # o momento é o tempo da avaliação
print(dataNotas.head())
print('')

print('Mostando as 5 primeiras Notas')
print(dataNotas["notas"].head()) # data serie
print('')

print('Monstrando os tipos de Notas')
print(dataNotas["notas"].unique()) # mostra que as notas que vão de 0 até 5
print('')

print('Média das Notas')
print(dataNotas["notas"].mean()) # pega a média das notas
print('')

print('Resumo dos dados')
print(dataNotas.describe()) # vai descrever (fazer um resumo dos dados)
print('')

# média => (1 + 3 + 5) / 3 => 3
# mas, para salário e outras coisas não é muito bom, para isso usa a MEDIANA (50% 50%)