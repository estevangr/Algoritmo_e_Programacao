""" O custo ao consumidor de um carro novo é a soma do preço de fábrica com o 
percentual de lucro do distribuidor e dos impostos ao preço de fábrica. Faça
um programa que receba o preço de fábrica de um veículo, o percentual de lucro
do distribuidor e o percentual de impostos.
 Calcule e mostre:
    a) o valor correspondente ao lucro do distribuidor;
    b) o valor correspondente ao imposto;
    c) o preço final de veículo """

 #variaveis

lucrod, imposto, preçoBase, preçoFinal = 0,0,0,0

#algoritmo

preçoBase = float(input("Digite o preço base do carro a ser vendido: "))

lucrod = float(input("Qual será o percentual de lucro do distribuidor? "))

imposto = float(input("Qual percentual de impostos a ser tributado? "))


lucrod = preçoBase * (lucrod/100)
imposto = preçoBase * (imposto/100)
valorFinal =   preçoBase + lucrod + imposto

print(f"O valor final do carro será de: R${lucrod:,.2f}")
print(f"O valor calculado do imposto é de: R$ {imposto:,.2f}")
print(f"O valor final do carro será de: R${valorFinal:,.2f}")



