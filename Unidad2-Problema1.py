"""
Rosete Zepeda Ismael

Problema 1:
Calculadora de edad
Trabajas en una compañía que ofrece seguros de vida y de gastos médicos. La empresa está desarrollando una herramienta tecnológica, para que los agentes puedan calcular el monto de una póliza. Para dicho cálculo, se consideran varios factores de riesgo, entre los que se encuentra la edad. Por ello, el contratante debe llenar un formulario, incluyendo su fecha de nacimiento. Como primer reto, deberás calcular la edad del cliente al momento de la cotización.
•	La captura de la fecha de nacimiento debe ser en una sola cadena de texto con formato DD-MM-AAAA.
•	Validar que sea una fecha existente, si supera los 31 días o menor a 1 día de un mes, se deberá marcar como inválido.
•	El año de nacimiento debe ser mayor de 1900.
•	Validar si el cliente ya cumplió años en la fecha de captura o aún no.
•	Validar que no se puede dejar información en blanco o campos vacíos

"""


# Se importa la clase 'datetime' desde el módulo del mismo nombre.
from datetime import datetime

# La entrada se guarda como una cadena de texto
fecha_nacimiento_str = input("Ingresa la fecha de nacimiento DD/MM/AAAA: ")


try:
    # Se convierte la cadena de texto a un objeto 'datetime'.
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
    
    # Se obtiene la fecha y hora actuales al día de hoy
    fecha_actual = datetime.now()
    
    # Se realiza un cálculo inicial de la edad restando los años.
    edad = fecha_actual.year - fecha_nacimiento.year
    
    # Se ajusta la edad si el cumpleaños de este año aún no ha pasado.
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        # Si el cumpleaños no ha pasado, se resta 1 a la edad.
        edad -= 1
        
    #Imprimimos en consola la edad del cliente, el resultado
    print(f"La edad del cliente es: {edad} años.")


except ValueError:
    # Se imprime un mensaje de error si el formato de fecha es inválido.
    print("ERROR: El formato de la fecha es incorrecto. Por favor, usa DD/MM/AAAA.")
