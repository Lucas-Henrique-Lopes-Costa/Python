from sklearn.svm import LinearSVC # usando uma biblioteca para treinar a nossa inteligência artificial
# pelo longo?
# perna curta?
# faz auau?

# 0 = não 
# 1 = sim

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [0, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# porco = 1
# cachorro = 0

treinoCaracteristicas = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3] # com esses dados
classificações = [1, 1, 1, 0, 0, 0] # classifique se é um porco ou cachorro

modelo = LinearSVC()
modelo.fit(treinoCaracteristicas, classificações) # encaixa esses dados no seu cérebro

animal_misterioso = [1, 1, 1]

# só que esse exemplo já foi passado no começo, então será como se ele estive apenas decodado

modelo.predict([animal_misterioso]) # ele vai predizer qual é o animal usando uma lista de animais

# para treinar a máquina para ela realmente "aprender" é preciso de mais exemplos

# pelo longo?
# perna curta?
# faz auau?

# 0 = não 
# 1 = sim
misterio1 = (0, 0, 0) # porco
misterio2 = (0, 0, 1) # cachorro
misterio3 = (0, 1, 0) # porco

treinoCaracteristicas = [misterio1, misterio2, misterio3]
classificação = [1, 0, 1] # eu sei que o primeiro é porco = 1 ou cachorro = 0

previsoes = modelo.predict(treinoCaracteristicas)
previsoes

# para saber o quão certo ele está
from sklearn.metrics import accuracy_score

taxa_de_acerto = int(accuracy_score(classificação, previsoes) * 100)
print('Sua taxa de acerto foi de ' + str(taxa_de_acerto) + "%")

# tentando melhorar o acerto

misterio1 = (0, 0, 1) # cachorro
misterio2 = (1, 0, 1) # cachorro
misterio3 = (1, 1, 0) # cachorro

treinoCaracteristicas = [misterio1, misterio2, misterio3]
classificação = [1, 1, 1] # eu sei que o primeiro é porco = 1 ou cachorro = 0

previsoes = modelo.predict(treinoCaracteristicas)
print(previsoes)

# para saber o quão certo ele está
from sklearn.metrics import accuracy_score

taxa_de_acerto = int(accuracy_score(classificação, previsoes) * 100)
print('Sua taxa de acerto foi de ' + str(taxa_de_acerto) + "%")