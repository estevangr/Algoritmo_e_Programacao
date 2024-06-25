""" //Faça um programa que receba o salário base de um funcionário.
Calcule e mostre o salário a receber, sabendo que esse funcionário tem gratificação
de R$ 50,00 e paga imposto de 10% sobre o salário base. """

#variaveis


salfinal, salbase = 0, 0

#algoritmo

salbase = float(input(" Digite o salário base do funcionário: "))

salfinal = salbase * 0.9 + 50

print(f"O salário final do funcionaro é de:  {salfinal}")
