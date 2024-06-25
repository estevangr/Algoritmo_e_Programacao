""" Faça um algoritmo que leia uma matriz 2 x 3 real
e depois imprima a matriz original e depois gere e
imprima sua matriz transposta (matriz 3 x 2 equivalente) """


#variaveis 

matriz = [[0]*3,[0]*3]

mat_trans = [[0]*2, [0]*2, [0]*2]

#algoritmo

for linha in range (0,2):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um numero para a posiçao {linha}, {coluna}:  "))

for linha in range (0,2):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]}]", end ='')
    print()

#transposta ->
for linha in range(0,3,1):
  for coluna in range(0,2,1):
    mat_trans[linha][coluna] = matriz[coluna][linha]

print("=====Mostrando a Matriz Transposta=====")                               
for linha in range(0,3,1):
  for coluna in range(0,2,1):
    print(f"[{mat_trans[linha][coluna]}]", end='')
  print()