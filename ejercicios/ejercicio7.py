numero = input("Escribe un numero y saldra su tabla de multiplicar")
numero = int(numero)

for x in range(1, 11):
    multiplicacion = numero * x
    #print(f'{x} * {numero} = {multiplicacion}')
    print(str(x) + " * " + str(numero) + " = " + str(multiplicacion))
