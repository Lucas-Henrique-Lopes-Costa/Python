import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula6.2/movies.csv"
filmes = pd.read_csv(uri) # data frame
filmes.columns = ["filmeId", "titulo", "generos"]
filmes = filmes.set_index('filmeId')
filmes = filmes.join(filmes['generos'].str.get_dummies()).drop('generos', axis=1)
filmes['ano'] = filmes['titulo'].str.extract(r'.*\((\d+)\)')
filmes = filmes.dropna()
filmes.head()

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula6.2/ratings.csv"
notas = pd.read_csv(uri)
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
arredondadas = notas['nota'].round(1)

medias = notas.groupby('filmeId')['nota'].mean()
filmes = filmes.join(medias).dropna().sort_values('nota', ascending=False).rename(columns={'nota' : 'media'})

total = notas.groupby('filmeId')['momento'].count()
filmes = filmes.join(total)
filmes = filmes.rename(columns={'momento' : 'total'})
filmes = filmes.query('total > 50')
filmes['media_categoria'] = (filmes['media']).round(1).values

random_filmes = filmes.sample(10)
# random_filmes.head()

filmes.head()

notas.head()

random_filmes

notas.describe()

notas['nota'].hist() # muita gente escolhe o número 4

# arredondadas.value_counts().plot.pie() # ele é muito ruim para visualizar para comparar | PARA COMPARAR DADOS TEM QUE USAR DADOS

plt.title("Destrunuição das Notas")
sns.countplot(arredondadas)

palette = sns.color_palette("Blues", 10) # usando o https://seaborn.pydata.org/tutorial/color_palettes.html para colocar cores diferente
sns.countplot(arredondadas, palette=palette)

sns.distplot(filmes['media']) # tentativa de expressar na vidad real

p = sns.barplot(data = random_filmes, x = 'titulo', y = 'media')
p.set_xticklabels(p.get_xticklabels(), rotation = 45, horizontalalignment = 'right')
plt.title('Notas médias de 10 filmes')
plt.show()

p = sns.barplot(data = random_filmes, x = 'titulo', y = 'media')
p.set_xticklabels(p.get_xticklabels(), rotation = 45, horizontalalignment = 'right')
plt.title('Notas médias de 10 filmes')
plt.ylim(2.5, 4) # é diferente de 0
plt.show()

# analizando de acordo com uma categoria
sns.catplot(data = filmes, x='Action', y='media')

sns.distplot(filmes.query("Action == 1")['media'])
sns.distplot(filmes.query("Action == 0")['media'])

ids_aleatorios = ",".join(random_filmes.index.values.astype(str))
query = f"filmeId in ({ids_aleatorios})"
query

sns.boxplot(data = notas.query(query), x = 'filmeId', y = 'nota')
plt.show()
# as barras são o limite e a barra preenchida é os 50%

total_de_categorias =  len(filmes['media_categoria'].unique())
sns.catplot(data=filmes, x='ano', y='media', palette = sns.color_palette('Blues', total_de_categorias), hue = 'media_categoria')