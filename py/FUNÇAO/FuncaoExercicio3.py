# Faça uma função que informe a quantidade de 
# dígitos de uma determinada frase informada.

frase = ""
digitos = 0

def num_digitos(x):
    digitos = len(x)
    return digitos

frase = str(input("Diga alguma frase: "))
digitos = num_digitos(frase) 

print(f"O número de dígitos nessa frase é: {digitos}")

#def cont_digitos(x):
    #return len(str(x))


#result = cont_digitos("IFSP Votuporanga")
#print(f"Quantidade de letras: {result}")
