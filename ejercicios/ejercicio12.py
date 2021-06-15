#palabra = "Josue"

# for letra in palabra:
#    print(letra)

frase = input("igrese una frase o palabra: ")
letra = input("ingrese a letra a buscar: ")

frase = frase.upper()
letra = letra.upper()
count = 0
for e in frase:
    if e == letra:
        count += 1

print(count)
