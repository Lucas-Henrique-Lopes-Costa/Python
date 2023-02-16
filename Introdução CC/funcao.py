numero = int(input("Qual valor do número binominal? "))
k = int(input("Qual valor do número k? "))

def fatorial(n):
  fat = 1
  if n < 0:
    return("Não possui fatorial para esse número.")

  while (n>1):
    fat = fat*n
    n -= 1
  return fat

def numero_binominal(n, k):
  if n < k:
    return("O número tem que ser maior que k.")
  return fatorial(n) // (fatorial(k) * fatorial(n-k))

print(numero_binominal(numero, k))
