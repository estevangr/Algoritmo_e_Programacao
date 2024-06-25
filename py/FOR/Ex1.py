# Construir um algoritmo que solicite um número e calcule a tabuada deste número

#variaveis

n = 0, 0

#algoritmo

n = int(input("Digite um numero para ser calculada a tabuada: "))


for i in range(0,n, 1):         #define o valor de i no proprio laço, assim não é necessario declarar a variavel anteriormente
    print(f"{n} * {i} = { n * i}")


    


# ---------------- Forma 2 -------------------------

#variaveis

i, n = 0, 0 #define o valor de i anteriormente ao algoritmo

#algoritmo

n = int(input("Digite um numero para ser calculada a tabuada: "))

for i in range(i,n, 1):     #(valor de inicio)(valor final)(passo)
    print(f"{n} * {i} = { n * i}")

