# Matriz de datos: [ID Cliente, Duración (segundos), Eventos Clics]
sesiones = [
    [1001, 200, 10],
    [1002, 45,  2],
    [1003, 120, 5],
    [1004, 190, 9],
    [1005, 30,  1]
]

# Módulo para clasificar el compromiso
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# Generar informe
print("=" * 40)
print("   INFORME DE NIVEL DE COMPROMISO")
print("=" * 40)
print(f"{'ID Cliente':<12} {'Duración(s)':<14} {'Clics':<8} {'Clasificación'}")
print("-" * 40)

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion   = sesion[1]
    clics      = sesion[2]
    nivel      = clasificar_compromiso(duracion, clics)
    print(f"{id_cliente:<12} {duracion:<14} {clics:<8} {nivel}")

print("=" * 40)