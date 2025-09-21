"""
ROSETE ZEPEDA ISMAEL Unidad 1. Introducción a Python y estructuras de control  
Problema:
Cajero automático
Has sido contratado por un banco que está en proceso de actualizar el software de sus cajeros automáticos. Tu tarea es desarrollar un algoritmo básico que simule el funcionamiento de un cajero automático, tomando como referencia las siguientes condiciones:

•	Entregar siempre la menor cantidad de billetes posible.
•	Mantener un inventario que indique cuál es la cantidad de billetes
•	disponible por cada denominación.
•	Las denominaciones disponibles son: 50, 100, 200, 500 y 1000.
•	Si el inventario no cuenta con una combinación de billetes suficientes para satisfacer el importe solicitado, no dispensará ningún billete.
•	Siempre que inicie el algoritmo, deberá haber en inventario 10 billetes de cada denominación.

"""

# Definir el inventario de billetes
inventario_billetes = {
    1000: 10,
    500: 10,
    200: 10,
    100: 10,
    50: 10
}

# Definir el orden de las denominaciones de mayor a menor
denominaciones = [1000, 500, 200, 100, 50]

# --- Función para retirar dinero ---
def retirar_dinero():
    monto_solicitado = input("Ingrese el monto a retirar (múltiplo de 50): ")
    
    # 1. Verificar si la entrada es un número válido
    try:
        monto_solicitado = int(monto_solicitado)
    except ValueError:
        print("Error: Por favor, ingrese un número.")
        return

    # 2. Verificar que el monto sea un múltiplo de 50
    if monto_solicitado <= 0 or monto_solicitado % 50 != 0:
        print("Error: El monto debe ser un número positivo y múltiplo de 50.")
        return

    # 3. Preparar los billetes a entregar y una copia del inventario
    billetes_a_entregar = {}
    monto_restante = monto_solicitado
    
    # Esta copia nos permite "probar" sin cambiar el inventario real
    inventario_temporal = inventario_billetes.copy()

    # 4. Calcular los billetes necesarios, empezando por los más grandes
    for billete in denominaciones:
        if monto_restante == 0:
            break
        
        # Calcular cuántos billetes de esta denominación podemos usar
        cantidad_necesaria = min(monto_restante // billete, inventario_temporal[billete])
        
        if cantidad_necesaria > 0:
            billetes_a_entregar[billete] = cantidad_necesaria
            monto_restante -= cantidad_necesaria * billete
            inventario_temporal[billete] -= cantidad_necesaria
    
    # 5. Comprobar si se pudo completar la transacción
    if monto_restante == 0:
        # ¡Éxito! Actualizar el inventario real
        global inventario_billetes
        inventario_billetes = inventario_temporal
        print(f"Transacción exitosa. Se le entregan ${monto_solicitado} en los siguientes billetes:")
        for billete, cantidad in billetes_a_entregar.items():
            print(f"  - {cantidad} billete(s) de ${billete}")
        print(f"\nInventario restante: {inventario_billetes}")
    else:
        # No hay suficientes billetes, no se entrega nada
        print("No hay suficientes billetes para este monto. Por favor, intente con otra cantidad.")

# --- Ejecutar el programa ---
print("Bienvenido al Cajero Automático")
retirar_dinero()
