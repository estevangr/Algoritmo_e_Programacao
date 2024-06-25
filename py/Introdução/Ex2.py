""" Faça um programa que receba uma medida em pés.
Faça as conversões a seguir e mostre os resultados em.
    a) polegadas
    b) jardas
    c) milhas
Sabe-se que:
    1 pé = 12 polegadas
    1 jarda = 3 pés
    1 milha = 1760 jardas """

#variaveis

polegada, milha, jarda, pe, valor = 0,0,0,0,0

#algoritmo

valor = float(input(" Digite uma distancia em pés: "))

pe = valor

polegada = 12 * pe
jarda = 3 * pe
milha = 1760 * jarda

print(f" O valor digitado em polegadas é: {polegada} ")
print(f" O valor digitado em milhas é: {milha} ")
print(f" O valor digitado em jardas é: {jarda} ")




