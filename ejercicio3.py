puntuacion = input("Cual es tu puntuacion? ")
puntuacion = float(puntuacion)  # decimales
ganancia = 2400 * puntuacion
mostrar_ganancia = True
# 0.4
if puntuacion == 0.0:
    print("Inaceptable")
elif puntuacion == 0.4:
    print("Aceptable")
elif puntuacion >= 0.6:
    print("Meritorio")
else:
    print("Valor invalido")
    mostrar_ganancia = False

if mostrar_ganancia == True:
    print(ganancia)
