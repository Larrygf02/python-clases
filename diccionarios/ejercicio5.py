cursos = {
    "matematica": 6,
    "fisica": 4,
    "quimica": 5
}

# for key in cursos.keys():
#    print(key + " tiene " + str(cursos[key]) + " creditos")

print(cursos.items())
total = 0
for key, value in cursos.items():
    total += value
    print(key + " tiene " + str(value) + " creditos")

print("Creditos totales " + str(total))
