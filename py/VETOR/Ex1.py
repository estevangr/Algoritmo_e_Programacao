""" Criar um algoritmo que receba 5 números inteiros,
armazene em um vetor e depois mostre o vetor na tela. """

#variaveis

vetor=[0]*5 # ou vetor = [0,0,0,0,0]


#algoritmo

for coluna in range(0,5,1):
    vetor[coluna] = int(input(f"Informe o número para a posição {coluna}: "))
                                
for coluna in range(0,5,1):
    print(f"[{vetor[coluna]}]", end='')