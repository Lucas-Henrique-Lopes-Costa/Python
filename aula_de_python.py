name = "Michel"
print(name)

idade = 21
def mais_um_ano(idade):
  print('Estou dentro da função')
  return idade + 1

mais_um_ano(21)

filmes = ["Toy Stort", "Xuxa", "Matrix"]

def imprime_filmes(filmes_que_quero_assistir):
  print('A lista de filmes é: ')
  print(filmes)

imprime_filmes(filmes)

filmes[1]

filmes[-1]

filmes[1:] # do 2º para frente

for filme in filmes:
  print(filme)

def imprime_filmes_em_linha(filmes_que_quero_imprimir):
  print('A lista de filmes é: ')
  for filme in filmes:
    print(filme)

print(imprime_filmes_em_linha(filmes))

dados = {
    "nome" : "Lucas",
    "idade" : 17,
    "empresa" : "LucasFilmes"
}
dados

dados["nome"]