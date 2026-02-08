# Pedimos el nombre al usuario
nombre = input("¿Cómo te llamas? ")

# Corregimos el saludo: quitamos espacios y ponemos la primera letra en mayúscula
nombre_corregido = nombre.strip().capitalize()

# Mostramos el resultado final
print(f"¡Hola, {nombre_corregido}! Es un gusto saludarte.")