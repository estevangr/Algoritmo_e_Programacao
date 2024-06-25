""" Calcular a quantidade de litros de combustível gastos em uma
viagem. Para obter o cálculo, o usuário deverá fornecer o
tempo gasto, quantos Km/l o carro faz e a velocidade média
durante a viagem. O programa deverá apresentar os valores da
velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade
de litros utilizados na viagem. """

#variaveis

vMedia, tempo, dist, consumo, kmLitro = 0,0,0,0,0

#algoritmo

tempo = float(input("Quanto tempo levou a viagem (em horas) ?"))

kmLitro = float(input("Quantos Km/l o carro está fazendo?"))

vMedia = float(input("Qual foi a velocidade media do veiculo? (Km/hora)"))

dist = vMedia * tempo

consumo = dist / kmLitro

print(f" Velocidade média: {vMedia}")
print(f" Duração da viagem: {tempo}")
print(f" Distancia percorrida da viagem: {dist}")
print(f" Consumo (litros gastos na viagem): {consumo}")




