from datetime import datetime

# 1. Obtenemos la hora actual del sistema
hora = datetime.now().hour

# 2. Definimos el saludo según el momento del día
if 5 <= hora < 12:
    momento = "Buenos días"
elif 12 <= hora < 20:
    momento = "Buenas tardes"
else:
    momento = "Buenas noches"

# 3. Pedimos el nombre y lo corregimos (limpieza de espacios y mayúsculas)
nombre = input("Dime tu nombre: ").strip().title()

# 4. Resultado final elegante
print(f"¡{momento}, {nombre}! Qué alegría verte por aquí.")