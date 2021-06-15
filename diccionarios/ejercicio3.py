frutas = {
    "platano": 1.35,
    "manzana": 0.8,
    "pera": 0.85,
    "naranja": 0.7
}

fruta = input("Que fruta desea llevar cacera: ")
fruta = fruta.lower()  # convierte toda la frase minuscula

if fruta in frutas:
    kilos = input("Cuantos kilos va a llevar caserita: ")
    kilos = int(kilos)
    pago = frutas[fruta] * kilos
    pago = round(pago, 2)
    print("El pago es ", str(pago))
else:
    print("Caserita no tengo mañana temprano traigo")
