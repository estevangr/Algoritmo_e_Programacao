n1 = 0
n2= 0
resultado = 0

#função
def somar_numeros_com_retorno_3_parametros(numero1, numero2):
    resultado = numero1 + numero2
    return numero1, numero2, resultado

#algoritmo
n1, n2, resultado = somar_numeros_com_retorno_3_parametros(3,5)

print (f"1 parametro: (n1)")
print (f"2 parametro: (n2)")
print (f"3 parametro: (resultado)")