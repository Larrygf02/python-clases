persona = {
    "nombre": "Ernesto",
    "edad": 33,
    "email": "ernesto@gmail.com",
    "sexo": "M"
}  # Diccionarios o objetos

print(persona["nombre"])

# Agregar telefono
persona["telefono"] = "948832929"
print(persona)

# Cambiar data de una llave
persona["edad"] = 34
print(persona)

if "nombredd" in persona:
    print(persona["nombre"])

print(persona.keys())
print(persona.values())
