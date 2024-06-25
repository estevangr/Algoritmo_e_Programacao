""" Faça um algoritmo que receba o nome e duas notas de um aluno.
Calcule a média e ao final mostre o nome do aluno, a média e a sua situação.
Caso a média seja no mínimo 6, o aluno está aprovado, se a média for inferior a 6 e 
no mínimo 4 o aluno está de Exame e se a média for inferior a 4 o mesmo está reprovado. """

#variaveis

nome, situaçao = "", ""
nota1, nota2, media = 0, 0, 0

#algoritmo

nome = str(input("Qual o nome do aluno? "))

nota1 = float(input("Qual a sua 1 nota? "))

nota2 = float(input("Qual a sua 2 nota? "))

media = (nota1 + nota2) /2 

if (media >= 6):
    situaçao = "aprovado"
else:
    if (media <= 6) & ( media >=4):
        situaçao = "Em Exame"
    else:
        situaçao = "reprovado"



print(f"O aluno {nome} teve media final de: {media}")
print(f"Sua situação é: {situaçao}")


